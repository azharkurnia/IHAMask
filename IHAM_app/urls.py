from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^$', form_test, name='form'),
    url(r'^add_data/', add_order_data_to_models, name='add_data'),
    url(r'^get_city/', get_city, name='get_city'),
    url(r'^get_price/(?P<destination>.*)/', get_price, name='get_price'),
    url(r'^index/', index, name='index'),
    url(r'^check_code/', check_code, name='check_code'),
]
