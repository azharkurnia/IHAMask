from django.shortcuts import render
import http.client
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.
response = {}

def form_test(request):
    return render(request, 'formTest.html', response)

# Method untuk get data dari form order lalu masukkan ke models
def add_order_data_to_models(request):
    if(request.method == 'POST'):
        customerName = request.POST['name'] if request.POST['name'] != "" else "Anonymous"
        customerEmail = request.POST['email'] if request.POST['email'] != "" else "Anonymous"
        customerPhone = request.POST['phone'] if request.POST['phone'] != "" else "Anonymous"
        productQuantityA = request.POST['productQuantityA'] if request.POST['productQuantityA'] != "" else 0
        productQuantityB = request.POST['productQuantityB'] if request.POST['productQuantityB'] != "" else 0
        productQuantityA = int(productQuantityA)
        productQuantityA = int(productQuantityA)
        street = request.POST['street'] if request.POST['street'] != "" else "Anonymous"
        province = request.POST['province'] if request.POST['province'] != "" else "Anonymous"
        # city
        # customerAddress
        productPriceA = productQuantityA * 5000
        productPriceB = productQuantityB * 7000
        productPriceA = int(productPriceA)
        productPriceB = int(productPriceB)
        totalProductPrice = productPriceA + productPriceB
        # totalPrice
        print("productQuantityA " + str(productQuantityA))
        print("street " + str(street))
        print("province " + str(province))
        print("productPriceA " + str(productPriceA))
        print("productPriceB " + str(productPriceB))
        print("totalProductPrice " + str(totalProductPrice))

# Method untuk dapatkan semua list provinsi
def get_province(request):
    conn = http.client.HTTPSConnection("api.rajaongkir.com")

    headers = { 'key': "ea827133edd06f4d89a5296c0661c3e4" }

    conn.request("GET", "/starter/province", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return JsonResponse(data)
