from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import PromoCode
from IHAM_app.models import OrderList, FAQ, upcomingEvents
from django.http import HttpResponseRedirect
# Create your views here.
response = {}
def show_login(request):
	return render(request, 'registration/login.html', response)

@login_required
def logged_in(request):
	promoCodeList = PromoCode.objects.all()
	orderList = OrderList.objects.all()
	faq = FAQ.objects.all()
	upcomingevents = upcomingEvents.objects.all()
	response['promoCodeList'] = promoCodeList
	response['orderList'] = orderList
	response['FAQ'] = faq
	response['upcomingEvents'] = upcomingevents
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
		return HttpResponseRedirect('/login/adminIHA/#form promo')
	else:
		return HttpResponseRedirect('/login/adminIHA/')

@login_required
def add_event(request):
	if(request.method == 'POST'):
		response['eventName'] = request.POST['eventName']
		response['eventURL'] = request.POST['eventURL']
		response['eventDate'] = request.POST['eventDate']
		response['eventVenue'] = request.POST['eventVenue']
		eventList = upcomingEvents(eventName=response['eventName'],eventURL=response['eventURL'],eventDate=response['eventDate'],eventVenue=response['eventVenue'])
		eventList.save()
		return HttpResponseRedirect('/login/adminIHA/#form event')
	else:
		return HttpResponseRedirect('/login/adminIHA/')

@login_required
def add_faq(request):
	if(request.method == 'POST'):
		response['titleIndo'] = request.POST['titleIndo']
		response['titleEng'] = request.POST['titleEng']
		response['isiIndo'] = request.POST['isiIndo']
		response['isiEng'] = request.POST['isiEng']
		faqlist = FAQ(titleIndo=response['titleIndo'],titleEng=response['titleEng'],isiIndo=response['isiIndo'],isiEng=response['isiEng'])
		faqlist.save()
		return HttpResponseRedirect('/login/adminIHA/#form faq')
	else:
		return HttpResponseRedirect('/login/adminIHA/')

@login_required
def delete_code(request, code_id):
	PromoCode.objects.filter(id=code_id).delete()
	return HttpResponseRedirect('/login/adminIHA/#form promo')

@login_required
def delete_faq(request, code_id):
	FAQ.objects.filter(id=code_id).delete()
	return HttpResponseRedirect('/login/adminIHA/#form faq')

@login_required
def delete_event(request, code_id):
	upcomingEvents.objects.filter(id=code_id).delete()
	return HttpResponseRedirect('/login/adminIHA/#form event')

@login_required
def paidSlideTrue(request, paidTrue_id):
	print("slidepaid")
	o = OrderList.objects.get(id=paidTrue_id)
	o.paidFlage = True
	print("true")
	o.save()
	print("saved" + paidTrue_id)
	return render(request, 'logged_in.html', response)

@login_required
def paidSlideFalse(request, paidFalse_id):
	print("slidepaidf")
	o = OrderList.objects.get(id=paidFalse_id)
	o.paidFlage = False
	print("false")
	o.save()
	print("savedf" + paidFalse_id)
	return render(request, 'logged_in.html', response)

@login_required
def deliveredSlideFalse(request, deliveredFalse_id):
	print("slidedeliveredf")
	o = OrderList.objects.get(id=deliveredFalse_id)
	o.deliveredFlage = False
	print("false")
	o.save()
	print("savedf" + deliveredFalse_id)
	return render(request, 'logged_in.html', response)

@login_required
def deliveredSlideTrue(request, deliveredTrue_id):
	print("slidedelivered")
	o = OrderList.objects.get(id=deliveredTrue_id)
	o.deliveredFlage = True
	print("true")
	o.save()
	print("saved" + deliveredTrue_id)
	return render(request, 'logged_in.html', response)