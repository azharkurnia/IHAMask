from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import PromoCode
# Create your views here.
response = {}
def show_login(request):
	return render(request, 'regsitration/login.html', response)

@login_required
def logged_in(request):
	promoCodeList = PromoCode.objects.all()
	response['promoCodeList'] = promoCodeList
	return render(request, 'logged_in.html', response)

@login_required
def add_promo_code(request):
	if(request.method == 'POST'):
		response['code'] = request.POST['code']
		response['amount'] = request.POST['amount']
		promoCodeList = PromoCode(promoCode=response['code'],promoAmount=response['amount'])
		promoCodeList.save()
		return HttpResponseRedirect('/login/adminIHA/')
	else:
		return HttpResponseRedirect('/login/adminIHA/')