from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^$', form_test, name='form'),
    url(r'^add_data/', add_data, name='add_data'),
    url(r'^get_province/', get_province, name='get_province'),
]
