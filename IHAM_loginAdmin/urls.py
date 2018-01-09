from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^adminIHA/', logged_in, name = 'logged_in'),
]