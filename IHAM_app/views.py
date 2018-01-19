from django.shortcuts import render
import http.client
import json
from django.http import HttpResponse, JsonResponse
from .models import upcomingEvents, FAQ, OrderList
from IHAM_loginAdmin.models import PromoCode
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import ast

# Create your views here.
response = {}

def form_test(request):
    return render(request, 'formTest.html', response)

def index(request):
    response['events'] = upcomingEvents.objects.all()
    response['faq'] = FAQ.objects.all()
    return render(request, 'index.html', response)

# Method untuk get data dari form order lalu masukkan ke models
@csrf_exempt
def add_order_data_to_models(request):
    if(request.method == 'POST'):
        customerName = request.POST['data']#,'test')# if request.POST['name'] != "" else "Anonymous"
        print("customerName " + (customerName))
        customerEmail = request.POST['email'] if request.POST['email'] != "" else "Anonymous"
        customerPhone = request.POST['phone'] if request.POST['phone'] != "" else "Anonymous"
        productQuantityA = request.POST['productQuantityA'] if request.POST['productQuantityA'] != "" else 0
        productQuantityB = request.POST['productQuantityB'] if request.POST['productQuantityB'] != "" else 0
        productQuantityA = int(productQuantityA)
        productQuantityB = int(productQuantityB)
        street = request.POST['street'] if request.POST['street'] != "" else "Anonymous"

       # province = 
        city = request.POST('kota')# if request.POST.get('nama_kots') != "" else "Anonymous"

        customerAddress = request.POST['street'] if request.POST['street'] != "" else "Anonymous"
        productPriceA = productQuantityA * 5000
        productPriceB = productQuantityB * 7000
        productPriceA = int(productPriceA)
        productPriceB = int(productPriceB)
        totalProductPrice = productPriceA + productPriceB
        # totalPrice
        print("productQuantityA " + str(productQuantityA))
        print("productQuantityB " + str(productQuantityB))
        print("street " + str(street))
        print("city " + str(city))
        print("productPriceA " + str(productPriceA))
        print("productPriceB " + str(productPriceB))
        print("totalProductPrice " + str(totalProductPrice))
        print("productQuantityA " + str(productQuantityA))


# method untuk mendapatkan semua kota atau kabupaten
def get_city(request):

    conn = http.client.HTTPSConnection("api.rajaongkir.com")

    headers = { 'key': "ea827133edd06f4d89a5296c0661c3e4" }

    conn.request("GET", "/starter/city", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data_city = json.loads(data)
    print(data)
    return JsonResponse(data_city)


def get_price(request, destination):

    conn = http.client.HTTPSConnection("api.rajaongkir.com")
    print("destination " + destination)
    payload = "origin=22&destination="+destination+"&weight=1000&courier=jne"

    headers = {
        'key': "ea827133edd06f4d89a5296c0661c3e4",
        'content-type': "application/x-www-form-urlencoded"
        }

    conn.request("POST", "/starter/cost", payload, headers)

    res = conn.getresponse()
    data = res.read()
    cost_Data = json.loads(data.decode("utf-8"))
    print(data.decode("utf-8"))
    return JsonResponse(cost_Data)

@csrf_exempt
def check_code(request):
    # print(current_code)
    if(request.method == 'POST'):
        current_code = request.POST['code']
        email = request.POST['email_check']
        try:
            promo = PromoCode.objects.get(promoCode=current_code)
            promo = model_to_dict(promo)
            promo = ast.literal_eval(promo)
            # if OrderList.objects.filter(customerEmail=email_check).exists():
            if email=="a@b.com":
                return HttpResponse("email")
            return JsonResponse(promo)
        except PromoCode.DoesNotExist:
            promo = None
            print(promo)
            return HttpResponse(promo)

def model_to_dict(obj):
    data = serializers.serialize('json', [obj,])
    struct = json.loads(data)
    data = json.dumps(struct[0]["fields"])
    return data
