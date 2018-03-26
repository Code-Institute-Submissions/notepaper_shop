from django.conf.urls import url,include


from .views import *


urlpatterns = [
    url(r'^pens_list$', pens_list, name='pens_list'),
    url(r'^pencils_list$', pencils_list, name='pencils_list'),
    url(r'^paper_list$', paper_list, name='paper_list'),
    url(r'^product_list$', product_list, name='product_list'),
    url(r'^new_product$', new_product, name='new_product'),
    url(r'^pens_list_high$', pens_list_high, name='pens_list_high'),
    url(r'^pencils_list_high$', pencils_list_high, name='pencils_list_high'),
    url(r'^product_list_high$', product_list_high, name='product_list_high'),
    url(r'^paper_list_high$', paper_list_high, name='paper_list_high'),
    url(r'^pens_list_low$', pens_list_low, name='pens_list_low'),
    url(r'^pencils_list_low$', pencils_list_low, name='pencils_list_low'),
    url(r'^paper_list_low$', paper_list_low, name='paper_list_low'),
    url(r'^product_list_low$', product_list_low, name='product_list_low'),
    
    
    ]
    