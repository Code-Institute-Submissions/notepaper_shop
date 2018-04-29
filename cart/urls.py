from django.conf.urls import url,include
from .views import *


urlpatterns = [
    url(r'^add/$', add_to_cart, name='add_to_cart'),
    url(r'^view_cart', view_cart, name='view_cart'),
    url(r'^remove/(\d+)$', remove_from_cart, name='remove_from_cart'),
    url(r'^update/(\d+)$', update_quantity, name='update_quantity'),
    url(r'^coupon/apply$',apply_coupon,name="apply_coupon"),
     url(r'^addc/$', add_to_cart_product_list, name='add_to_cart_product_list'),
    
   
  
    

    ]