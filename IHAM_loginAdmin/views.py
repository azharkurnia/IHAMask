from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import PromoCode
from django.http import HttpResponseRedirect
# Create your views here.
response = {}
def show_login(request):
	return render(request, 'registration/login.html', response)

@login_required
def logged_in(request):
	promoCodeList = PromoCode.objects.all()
	response['promoCodeList'] = promoCodeList
	return render(request, 'logged_in.html', response)

@login_required
def add_promo_code(request):
	if(request.method == 'POST'):
		response['code'] = request.POST['code']
		print("code " + str(request.POST['code']))
		response['amount'] = request.POST['amount']
		print("amount " + str(request.POST['amount']))
		promoCodeList = PromoCode(promoCode=response['code'],promoAmount=response['amount'])
		promoCodeList.save()
		return HttpResponseRedirect('/login/adminIHA/')
	else:
		return HttpResponseRedirect('/login/adminIHA/')

@login_required
def delete_code(request, code_id):
	print("delete")
	PromoCode.objects.filter(id=code_id).delete()
	return HttpResponseRedirect('/login/adminIHA/')