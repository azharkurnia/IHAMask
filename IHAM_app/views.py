from django.shortcuts import render
import http.client
import json

# Create your views here.
response = {}

def form_test(request):
    response["provinces"] = get_province(request)['rajaongkir']['results']
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
    data = data.decode("utf-8")
    data = json.loads(data)
    return data
    # print(data.decode("utf-8"))
    # print(type(data))
    print(data['rajaongkir']['status']['description'])
    
