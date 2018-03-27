from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
# Create your views here.
def get_index(request):
    new_arrivals=Product.objects.order_by('created_date')[:10]
    
    
    return render(request,'home/index.html',{'new_arrivals':new_arrivals})
    
    
    
    
