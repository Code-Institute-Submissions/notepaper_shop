from django.conf.urls import url,include


from .views import *


urlpatterns = [
   
   
    url(r'^products_list/$', products_list, name='products_list'),
     url(r'^new_product$', new_product, name='new_product'),
  
    
    ]
    