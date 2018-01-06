from django.shortcuts import render

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
