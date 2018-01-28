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
  // $("#quantity-productB").val("");

  // $("#checkboxA").change(function(){
  //   $("#quantity-productA").toggle();   // Tampilkan input quantity ketika checkbox dipilih
  //   var display = $("#quantity-productA").attr("style");
  //   if (display.includes("none")) { //Kalo input field quantity di ilangin, value nya di reset juga
  //     $("#quantity-productA").val("");
  //   }
  //   updatePrice();
  // });
  // $("#checkboxB").change(function(){
  //   $("#quantity-productB").toggle();
  //   var display = $("#quantity-productB").attr("style");
  //   if (display.includes("none")) {
  //     $("#quantity-productB").val("");
  //   }
  //   updatePrice();
  // });

  // Setiap update kuantitas produk, update harga juga
  $("#quantity-productA").bind('keyup mouseup', function(){
    updatePrice();
  });
  // $("#quantity-productB").bind('keyup mouseup', function(){
  //   updatePrice();
  // });

  

    var form = $('#form');
    $(form).submit(function(event) {
      // Stop the browser from submitting the form.
      event.preventDefault();

      // TODO
      // Serialize the form data.]
      var nama = $("#InputName").val().toString();
      var email = $("#InputEmail").val().toString();
      var nomor_hp = $("#phone-number").val().toString();
      var productA = $("#quantity-productA").val().toString();
      var productB = "0";
      var alamat = document.getElementById("order-address").innerHTML.toString();
      var kodepos = $("#postal").val().toString();
      var kota = kotaUntukDataBase.toString();
      var kode_promo = $("#promotion-code").val().toString();
      var harga_barang = document.getElementById("harga-barang").innerHTML.toString();
      var harga_kurir = document.getElementById("ongkos-kirim").innerHTML.toString();
      var total_harga = document.getElementById("total-harga").innerHTML.toString();

      // Submit the form using AJAX.
      $.ajax({
        type: 'POST',
        url: $(form).attr('action'),
        data: {
          name : nama,
          email : email,
          phone : nomor_hp,
          productQuantityA : productA,
          productQuantityB : productB,
          street : alamat,
          kota : kota,
          promoCode : kode_promo,
          productPrice: harga_barang,
          shippingPrice : harga_kurir,
          totalPrice : total_harga
        },
        success: function(data){
          $('#exampleModal').modal('hide');
          $('#success').modal('show');
        },
        error: function(){
          alert("Failed");
          window.location.reload();
        }
      });
    });

    // Ajax untuk mendapat data provinsi dan ditampilkan dalam select province
    $.ajax({
        method: "GET",
        url: "/form/get_city/",
        async: false,
        success : function (data) {
            listCity = data['rajaongkir']['results'];
            for (var i = 0; i < listCity.length; i++) {
              listCity[i]['id'] = listCity[i]['city_id'];
              listCity[i]['text'] = listCity[i]['type'] + " " + listCity[i]['city_name'];
            }
            console.log(listCity);
            if (localStorage.getItem("listCity") === null) {
              localStorage.setItem("listCity", JSON.stringify(listCity));
            }
            $(".my-select-city").select2({
              placeholder: "Select Your Region",
              "data" : listCity
             });
        }
    });

   $("#submit-button").unbind('click').bind('click', function (e){
      e.preventDefault();
      if (document.getElementById("form").checkValidity()) {
      $('#dataConfirm').html ('<p>Name : '+ $("#InputName").val().toString()+'</p><br><p>Email : '+ $("#InputEmail").val().toString()+'</p><br><p>Phone Number : '+ $("#phone-number").val().toString()+'</p><br><p>Order qty : '+ $("#quantity-productA").val().toString()+'</p><br><p>Deliver To :'+ document.getElementById("order-address").innerHTML.toString()+'</p><br><p>Total Price : IDR '+ document.getElementById("total-harga").innerHTML.toString()+'</p>');
      var nama = $("#InputName").val().toString();
      var email = $("#InputEmail").val().toString();
      var nomor_hp = $("#phone-number").val().toString();
      var productA = $("#quantity-productA").val().toString();
      var productB = "0";
      var alamat = document.getElementById("order-address").innerHTML.toString();
      var kodepos = $("#postal").val().toString();
      var kota = kotaUntukDataBase.toString();
      var kode_promo = $("#promotion-code").val().toString();
      var harga_barang = document.getElementById("harga-barang").innerHTML.toString();
      var harga_kurir = document.getElementById("ongkos-kirim").innerHTML.toString();
      var total_harga = document.getElementById("total-harga").innerHTML.toString(); 
      document.getElementById("modalHidden").click(); 
      }
      else { document.getElementById("submitform").click(); }
    });


    $(".my-select-city").on('change', function (e){
      var index;
      var id_kota = $(".my-select-city").val();
      for (var i = 0; i < listCity.length; i++){
        if (listCity[i]['id'] == id_kota){
          index = i;
          kotaDipilih = listCity[i]
          break;
        }
      }

      console.log(kotaDipilih);
      updateAddress();
      $.ajax({
        method: "GET",
        url: "/form/get_price/" + (index+1) + "/",
        success : function(data) {
          console.log(data);
          var nama_kota = data['rajaongkir']['destination_details']['city_name'];
          kotaUntukDataBase = nama_kota;
          console.log(nama_kota);
          if ((data['rajaongkir']['results'][0]['costs']).length > 0) {
            try {
                var shipping_cost = data['rajaongkir']['results'][0]['costs'][1]['cost'][0]['value'];
            }
            catch(err) {
                var shipping_cost = data['rajaongkir']['results'][0]['costs'][0]['cost'][0]['value'];
            }
          } else {
              shipping_cost = 0;
          }
          getShippingCost(shipping_cost);
          updatePrice();

        }
      })
    });



    // Menampilkan halaman HTML [HARUS SELALU DIAKHIR DOCUMENT READY]
    $('#welcome').modal('show');



});

// Fungsi untuk get kuantitas
function getValueA(){
  var valueProductA = $("#quantity-productA").val();
  console.log(valueProductA);
  if (valueProductA != 0) {
    return parseInt(valueProductA);
  } else {
    return 0;
  }
}
// function getValueB(){
//   var valueProductB = $("#quantity-productB").val();
//   if (valueProductB != 0) {
//     return parseInt(valueProductB);
//   } else {
//     return 0;
//   }
// }

// Fungsi untuk get total harga parang
function getHargaBarang(){
  var hargaProductA = 89000;
  var hargaProductB = 7000;
  return ((getValueA() * hargaProductA));
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
    if (promo.includes("You got discount")) {
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

  var listCity;
  var i = 1;
  var city;
  var kotaDipilih;
  var kotaUntukDataBase;
  var updateAddress = function(){
    var street = $("#street").val();
    try {
      var city = kotaDipilih['text'];
      var province = kotaDipilih['province'];
      var postal_code = $("#postal").val();
      $("#order-address").text(street + " , " + city + " , " + province + " , " + postal_code);
    } catch (e) {
      $("#order-address").text(street);
    }
  }
  var email_checkPromo = function(){
    var current_code = $("#promotion-code").val();
    if (current_code != "") {
      check_promo();
    }
  }
  var check_promo = function(){
    var current_code = $("#promotion-code").val();
    var email = $("#InputEmail").val();
    $.ajax({
      method: "POST",
      url: "/form/check_code/",
    data: {code : current_code, email_check : email},
      success : function(data){
        console.log(data);
        if ((typeof data) == "object") {
          promoAmount = data['promoAmount'];
          $("#promo-icon").html("<p style='margin-bottom: 0;'>&#10004; You got discount <span id='promo-amount'>" + promoAmount + "</span> % of total price</p>");
        }
        else if (data === "email"){
          $("#promo-icon").html("<p>Promo code already used by this email &#10006;</p>");
        }
        else {
          if (current_code == "") {
            $("#promo-icon").html("");
          } else {
            $("#promo-icon").html("<p>&#10006;</p>");
          }
        }
        updatePrice();
      }
    });
  }