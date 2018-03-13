from django.shortcuts import render
import http.client
import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import upcomingEvents, FAQ, OrderList
from IHAM_loginAdmin.models import PromoCode
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import ast
from django.conf import settings
from django.core.mail import send_mail

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
        customerName = request.POST['name'] if request.POST['name'] != "" else "Anonymous"
        customerEmail = request.POST['email'] if request.POST['email'] != "" else "Anonymous"
        customerPhone = request.POST['phone'] if request.POST['phone'] != "" else "Anonymous"
        productQuantityA = request.POST['productQuantityA'] if request.POST['productQuantityA'] != "" else 0
        productQuantityB = request.POST['productQuantityB'] if request.POST['productQuantityB'] != "" else 0
        promoCode = request.POST['promoCode'] if request.POST['promoCode'] != '' else "no-code-submitted"
        productPrice = request.POST['productPrice'] if request.POST['productPrice'] != "" else 0
        shippingPrice = request.POST['shippingPrice'] if request.POST['shippingPrice'] != "Sorry JNE can't reach your city yet" else 0
        grandTotalPrice = request.POST['totalPrice'] if request.POST["totalPrice"] != "" else 0

        productQuantityA = int(productQuantityA)
        productQuantityB = int(productQuantityB)
        productPrice = int(productPrice)
        shippingPrice = int(shippingPrice)
        grandTotalPrice = int(grandTotalPrice)


        customerAddress = request.POST['street'] if request.POST['street'] != "" else "Anonymous"
        city = request.POST['kota'] if request.POST['kota'] != "" else "Anonymous"

        print("productQuantityA " + str(productQuantityA))
        print("productQuantityB " + str(productQuantityB))
        print("street " + str(customerAddress))
        print("city " + str(city))
        # print("productPriceA " + str(productPriceA))
        # print("productPriceB " + str(productPriceB))
        # print("totalProductPrice " + str(totalProductPrice))
        # print("productQuantityA " + str(productQuantityA))
        print("shippingPrice " + str(shippingPrice))

        order = OrderList(
            customerName = customerName,
            customerEmail = customerEmail,
            customerPhone = customerPhone,
            productQuantityA=productQuantityA,
            productQuantityB = productQuantityB,
            customerAddress = customerAddress,
            productPrice = productPrice,
            shippingPrice = shippingPrice,
            grandTotalPrice = grandTotalPrice,
            promoCode = promoCode
            )
        order.save()

        #JALANIN SEND EMAIL DISINI
        # email = EmailMessage('title', 'body', to=[email])
        # email.send()
        email_content='''<HTML>
        <HEAD>
            <META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">
            <TITLE></TITLE>
            <META NAME="GENERATOR" CONTENT="LibreOffice 4.1.6.2 (Linux)">
            <META NAME="CREATED" CONTENT="20180313;10500000000000">
            <META NAME="CHANGEDBY" CONTENT="Favian Kharisma Hazman">
            <META NAME="CHANGED" CONTENT="20180313;10600000000000">
            <META NAME="AppVersion" CONTENT="16.0000">
            <META NAME="DocSecurity" CONTENT="0">
            <META NAME="HyperlinksChanged" CONTENT="false">
            <META NAME="LinksUpToDate" CONTENT="false">
            <META NAME="ScaleCrop" CONTENT="false">
            <META NAME="ShareDoc" CONTENT="false">
            <STYLE TYPE="text/css">
            <!--
                @page { size: 8.5in 11in; margin: 1in }
                P { margin-bottom: 0.08in; direction: ltr; widows: 2; orphans: 2 }
            -->
            </STYLE>
        </HEAD>
        <BODY LANG="en-US" DIR="LTR">
        <P ALIGN=JUSTIFY STYLE="margin-bottom: 0in">Halo <I>Dear,</I> 
        </P>
        <P ALIGN=JUSTIFY STYLE="text-indent: 0.5in; margin-bottom: 0in">Terima
        kasih karena telah membantu kami melestarikan alam dan mempercayakan
        kulit cantikmu pada <B>IHA Mask</B>! Hanya dengan <B>Rp 89.000,00</B>
        saja kamu bisa mendapatkan kulit sehat dan cerah dalam sekejap.
        Jangan lupa segera lakukan pembayaran ke nomor rekening berikut:</P>
        <P ALIGN=JUSTIFY STYLE="margin-bottom: 0in"><BR>
        </P>
        <P ALIGN=CENTER STYLE="margin-bottom: 0in"><B>8700175198</B></P>
        <P ALIGN=CENTER STYLE="margin-bottom: 0in"><B>BCA</B></P>
        <P ALIGN=CENTER STYLE="margin-bottom: 0in"><B>A/N Muhammad Fachry</B></P>
        <P ALIGN=JUSTIFY STYLE="margin-bottom: 0in"><BR>
        </P>
        <P ALIGN=JUSTIFY STYLE="margin-bottom: 0in">    Jika sudah melakukan
        pembayaran, segera kirimkan bukti transfer-mu dengan membalas e-mail
        ini selambat-lambatnya empat hari setelah pemesanan agar pengiriman
        dapat segera diproses. Sudah tidak sabar ‘kan untuk merawat kulit
        cantikmu? <I>Happy shopping! </I>
        </P>
        <P ALIGN=CENTER STYLE="margin-bottom: 0in"><BR>
        </P>
        <P ALIGN=CENTER STYLE="margin-bottom: 0in"><BR>
        </P>
        <P ALIGN=RIGHT STYLE="margin-bottom: 0in"><I>Nature to get better,</I></P>
        <P ALIGN=RIGHT STYLE="margin-bottom: 0in"><I>Have a nice day!</I></P>
        <P ALIGN=RIGHT STYLE="margin-bottom: 0in"><BR>
        </P>
        </BODY>
        </HTML>'''
        msg = EmailMessage("Terima Kasih Telah Memesan IHAMASK!", email_content, settings.EMAIL_HOST_USER, [customerEmail])
        msg.content_subtype = "html"
        msg.send()
        return HttpResponse("Complete")

#export data orderan to json
def OrderListToJSON(request):
    data = OrderList.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

# method untuk mendapatkan semua kota atau kabupaten
def get_city(request):

    conn = http.client.HTTPSConnection("api.rajaongkir.com")

    headers = { 'key': "ea827133edd06f4d89a5296c0661c3e4" }

    conn.request("GET", "/starter/city", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data_city = json.loads(data)
    # print(data)
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
    data = data.decode("utf-8")
    cost_Data = json.loads(data)
    return JsonResponse(cost_Data)

@csrf_exempt
def check_code(request):
    if(request.method == 'POST'):
        current_code = request.POST['code']
        email = request.POST['email_check']
        try:
            promo = PromoCode.objects.get(promoCode=current_code)
            promo = model_to_dict(promo)
            promo = ast.literal_eval(promo)
            if OrderList.objects.filter(customerEmail=email).exists():
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
