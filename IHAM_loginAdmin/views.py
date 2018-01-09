from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.
response = {}

def show_login(request):
    return render(request, 'regsitration/login.html', response)

@login_required
def logged_in(request):
    return render(request, 'logged_in.html', response
    )