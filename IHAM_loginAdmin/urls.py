from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^adminIHA/', logged_in, name = 'logged_in'),
    url(r'^add_promo_code/', add_promo_code, name = 'add_promo_code'),
    url(r'^add_event/', add_event, name = 'add_event'),
    url(r'^add_FAQ/', add_faq, name = 'add_faq'),
    url(r'^delete_code/(?P<code_id>[0-9]+)/$', delete_code, name='delete_code'),
    url(r'^delete_faq/(?P<code_id>[0-9]+)/$', delete_faq, name='delete_faq'),
    url(r'^delete_event/(?P<code_id>[0-9]+)/$', delete_event, name='delete_event'),
    url(r'^delete_order/(?P<order_id>[0-9]+)/$', delete_order, name='delete_order'),
    url(r'^paidSlide/(?P<paid_id>[0-9]+)/$', paidSlide, name='paidSlide'),
    url(r'^deliveredSlide/(?P<delivered_id>[0-9]+)/$', deliveredSlide, name='deliveredSlide'),
]