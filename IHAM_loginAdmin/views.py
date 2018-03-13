from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
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
def delete_order(request, order_id):
	print("delete_order")
	OrderList.objects.filter(id=order_id).delete()
	return HttpResponseRedirect('/login/adminIHA/')

@login_required
def paidSlide(request, paid_id):
	print("slidepaid")
	o = OrderList.objects.get(id=paid_id)
	if (o.paidFlage):
		o.paidFlage = False
		print("false")
	else:
		o.paidFlage = True
		print("true")
		email_content='''<HTML>
					     <HEAD>
						<META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">
						<TITLE></TITLE>
						<META NAME="GENERATOR" CONTENT="LibreOffice 4.1.6.2 (Linux)">
						<META NAME="CREATED" CONTENT="20180313;10500000000000">
						<META NAME="CHANGEDBY" CONTENT="Favian Kharisma Hazman">
						<META NAME="CHANGED" CONTENT="20180313;11900000000000">
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
						<P ALIGN=JUSTIFY STYLE="margin-bottom: 0in">Halo <I>Dear</I>,</P>
						<P ALIGN=JUSTIFY STYLE="margin-bottom: 0in"><A NAME="_gjdgxs"></A>	Selamat!
						Pembayaranmu telah berhasil. Terima kasih karena telah mempercayakan
						kulit cantikmu pada <B>IHA Mask</B>. Pengiriman <B>IHA</B>-mu akan
						segera kami proses selambat-lambatnya tiga hari setelah pembayaran.
						Sudah tidak sabar ‘kan untuk memberikan perawatan terbaik untuk
						kulit-mu?</P>
						<P ALIGN=JUSTIFY STYLE="margin-bottom: 0in"><BR>
						</P>
						<P ALIGN=JUSTIFY STYLE="margin-bottom: 0in"><BR>
						</P>
						<P ALIGN=RIGHT STYLE="margin-bottom: 0in"><I>Nature to get better, </I>
						</P>
						<P ALIGN=RIGHT STYLE="margin-bottom: 0in"><I>Have a nice day!</I></P>
						</BODY>
						</HTML>'''
		msg = EmailMessage("Konfirmasi Pembayaran IHAMASK!", email_content, settings.EMAIL_HOST_USER, [customerEmail])
		msg.content_subtype = "html"
		msg.send()
	o.save()
	print("saved " + paid_id)
	return render(request, 'logged_in.html', response)

@login_required
def deliveredSlide(request, delivered_id):
	print("slidedelivered")
	o = OrderList.objects.get(id=delivered_id)
	if (o.deliveredFlage):
		o.deliveredFlage = False
		print("false")
	else:
		o.deliveredFlage = True
		print("true")
		email_content='''<HTML>
						<HEAD>
							<META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">
							<TITLE></TITLE>
							<META NAME="GENERATOR" CONTENT="LibreOffice 4.1.6.2 (Linux)">
							<META NAME="CREATED" CONTENT="20180313;10500000000000">
							<META NAME="CHANGEDBY" CONTENT="Favian Kharisma Hazman">
							<META NAME="CHANGED" CONTENT="20180313;13300000000000">
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
						<P ALIGN=JUSTIFY STYLE="margin-bottom: 0in">Halo <I>Dear</I>,</P>
						<P ALIGN=JUSTIFY STYLE="margin-bottom: 0in">	Akhirnya saat yang
						ditunggu-tunggu datang juga nih! Kami telah mengirimkan <B>IHA Mask</B>
						ke seluruh penjuru Indonesia, termasuk kamu. Jangan lupa kabari kami
						apabila barang telah diterima. Oh! Kami juga akan merasa sangat
						senang dan terhormat apabila bisa mendapat<I> review</I> mengenai <B>IHA
						Mask</B> dari kamu, ditunggu ya! Selamat memanjakan kulit cantikmu
						dengan <B>IHA Mask</B> ☺</P>
						<P ALIGN=JUSTIFY STYLE="margin-bottom: 0in"><A NAME="_GoBack"></A><BR>
						</P>
						<P ALIGN=RIGHT STYLE="margin-bottom: 0in"><I>Nature to get better,</I></P>
						<P ALIGN=RIGHT STYLE="margin-bottom: 0in"><I>Have a nice day!</I></P>
						</BODY>
						</HTML>'''
		msg = EmailMessage("IHAMASK Anda Telah Dikirim!", email_content, settings.EMAIL_HOST_USER, [customerEmail])
		msg.content_subtype = "html"
		msg.send()
	o.save()
	print("saved " + delivered_id)
	return render(request, 'logged_in.html', response)