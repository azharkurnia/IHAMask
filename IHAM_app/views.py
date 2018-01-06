from django.shortcuts import render
import http.client

# Create your views here.
response = {}

def form_test(request):
    return render(request, 'formTest.html', response)

def add_data(request):
    form = Message_Form(request.POST or None)
    if(request.method == 'POST'):
        response['name'] = request.POST['name'] if request.POST['name'] != "" else "Anonymous"
        response['email'] = request.POST['email'] if request.POST['email'] != "" else "Anonymous"
        print(response['name'])

def get_province(request):
    conn = http.client.HTTPSConnection("api.rajaongkir.com")

    headers = { 'key': "ea827133edd06f4d89a5296c0661c3e4" }

    conn.request("GET", "/starter/province", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
