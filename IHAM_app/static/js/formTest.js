$(document).ready(function(){
  $("#checkboxA").change(function(){
    $("#quantity-productA").toggle();
    var display = $("#quantity-productA").attr("style");
    if (display.includes("none")) {
      $("#quantity-productA").val("");
    }
    $("#harga-barang").text(getHargaBarang());
  });

  $("#checkboxB").change(function(){
    $("#quantity-productB").toggle();
    var display = $("#quantity-productB").attr("style");
    if (display.includes("none")) {
      $("#quantity-productB").val("");
    }
    $("#harga-barang").text(getHargaBarang());
  });

  $("#quantity-productA").keyup(function(){
    $("#harga-barang").text(getHargaBarang());
  });

  $("#quantity-productB").keyup(function(){
    $("#harga-barang").text(getHargaBarang());
  });
});

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

function getHargaBarang(){
  var hargaProductA = 5000;
  var hargaProductB = 7000;
  return ((getValueA() * hargaProductA) + (getValueB() * hargaProductB));
}
