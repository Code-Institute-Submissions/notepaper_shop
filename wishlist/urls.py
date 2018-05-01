from django.conf.urls import url,include
from wishlist.views import *


urlpatterns = [
    url(r'^add/$', add_to_wishlist, name='add_to_wishlist'),
    url(r'^view_wishlist', view_wishlist, name='view_wishlist'),
    
  
    
   
  
    

    ]