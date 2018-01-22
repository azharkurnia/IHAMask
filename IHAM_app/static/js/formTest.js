// refresh halaman jika user back pada browser
window.addEventListener( "pageshow", function ( event ) {
  var historyTraversal = event.persisted || ( typeof window.performance != "undefined" && window.performance.navigation.type === 2 );
  if ( historyTraversal ) {
    // Handle page restore.
    window.location.reload();
  }
});

$(document).ready(function(){



  // Memastikan value kuantitas nol di awal
  var shipping_cost;
  $("#quantity-productA").val("");
  $("#quantity-productB").val("");

  $("#checkboxA").change(function(){
    $("#quantity-productA").toggle();   // Tampilkan input quantity ketika checkbox dipilih
    var display = $("#quantity-productA").attr("style");
    if (display.includes("none")) { //Kalo input field quantity di ilangin, value nya di reset juga
      $("#quantity-productA").val("");
    }
    updatePrice();
  });
  $("#checkboxB").change(function(){
    $("#quantity-productB").toggle();
    var display = $("#quantity-productB").attr("style");
    if (display.includes("none")) {
      $("#quantity-productB").val("");
    }
    updatePrice();
  });

  // Setiap update kuantitas produk, update harga juga
  $("#quantity-productA").bind('keyup mouseup', function(){
    console.log("change");
    updatePrice();
  });
  $("#quantity-productB").bind('keyup mouseup', function(){
    updatePrice();
  });


});

// Fungsi untuk get kuantitas
function getValueA(){
  var valueProductA = $("#quantity-productA").val();
  if (valueProductA != 0) {
    return parseInt(valueProductA);
  } else {
    return 0;
  }
}
function getValueB(){
  var valueProductB = $("#quantity-productB").val();
  if (valueProductB != 0) {
    return parseInt(valueProductB);
  } else {
    return 0;
  }
}

// Fungsi untuk get total harga parang
function getHargaBarang(){
  var hargaProductA = 89000;
  var hargaProductB = 7000;
  return ((getValueA() * hargaProductA) + (getValueB() * hargaProductB));
}

function getShippingCost(harga){
  if (harga == 0) {
      $("#ongkos-kirim").text("Sorry JNE can't reach your city yet");
  } else {
      $("#ongkos-kirim").text(harga);
  }
}

//Fungsi untuk tampilkan data pada select di form
function hi(province){
  $(".my-select-province").select2({
    "data" : province
  });
}
function updatePrice(){
  shipping_cost = $("#ongkos-kirim").text();
  product_price = getHargaBarang();
  shipping_cost = parseInt(shipping_cost);
  product_price = parseInt(product_price);
  promo = $("#promo-icon").text();
  total = 0;
  promo_amount = 0;
  if (promo != "") {
    console.log("masuk sini(1)");
    if (promo.length > 30) {
      console.log("masuk sini(2)");
      promo_amount = $("#promo-amount").text();
      console.log(promo_amount);
      promo_amount = parseInt(promo_amount);
      console.log(promo_amount);
      promo_amount = getDiscount(promo_amount);
      console.log(promo_amount);
      total = product_price + shipping_cost - promo_amount;
      console.log(total);
    } else {
      total = product_price + shipping_cost;
    }
  } else {
    total = product_price + shipping_cost;
  }
  product_price = product_price - promo_amount
  $("#harga-barang").text(product_price);
  $("#total-harga").text(total);
  return total;
}

function getDiscount(amount){
  shipping_cost = $("#ongkos-kirim").text();
  product_price = getHargaBarang();
  shipping_cost = parseInt(shipping_cost);
  product_price = parseInt(product_price);
  discount = ((amount / 100) * product_price);
  return discount;
}
