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
  $("#quantity-productA").val("");
  $("#quantity-productB").val("");

  $("#checkboxA").change(function(){
    $("#quantity-productA").toggle();   // Tampilkan input quantity ketika checkbox dipilih
    var display = $("#quantity-productA").attr("style");
    if (display.includes("none")) { //Kalo input field quantity di ilangin, value nya di reset juga
      $("#quantity-productA").val("");
    }
    $("#harga-barang").text(getHargaBarang());  //Selalu update harga barang
    $("#total-harga").text(getHargaBarang()); //Selalu update total harga
  });
  $("#checkboxB").change(function(){
    $("#quantity-productB").toggle();
    var display = $("#quantity-productB").attr("style");
    if (display.includes("none")) {
      $("#quantity-productB").val("");
    }
    $("#harga-barang").text(getHargaBarang());
    $("#total-harga").text(getHargaBarang());
  });

  // Setiap update kuantitas produk, update harga juga
  $("#quantity-productA").keyup(function(){
    $("#harga-barang").text(getHargaBarang());
    $("#total-harga").text(getHargaBarang());
  });
  $("#quantity-productB").keyup(function(){
    $("#harga-barang").text(getHargaBarang());
    $("#total-harga").text(getHargaBarang());
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
  var hargaProductA = 5000;
  var hargaProductB = 7000;
  return ((getValueA() * hargaProductA) + (getValueB() * hargaProductB));
}

 //Fungsi untuk tampilkan data pada select di form
 function hi(province){
   $(".my-select-province").select2({
     "data" : province

 });



}
