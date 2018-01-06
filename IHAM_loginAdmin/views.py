from django.shortcuts import render

# Create your views here.
response = {}

def show_login(request):
    return render(request, 'regsitration/login.html', response)