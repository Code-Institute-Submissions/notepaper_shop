from django.conf.urls import url,include


from .views import *


urlpatterns = [
    url(r'^pens_list', pens_list, name="pens_list"),
    url(r'^pencils_list', pencils_list, name="pencils_list"),
    url(r'^paper_list', paper_list, name="paper_list"),
    
  
     
   
    
    ]
    