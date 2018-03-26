from django.shortcuts import render,get_object_or_404,redirect
from products.models import Cart_items,Product,Coupon
from .forms import Cart_itemsForm,CouponForm
from .models import Cart_items,Coupon,Product

# Create your views here.
def pens_list(request):
    cart_items=Cart_items.objects.filter(item_class='PRODUCT',item_type='PEN')
    
    return render(request, 'products/product_list.html',{'cart_items':cart_items})

def pencils_list(request):
    cart_items=Cart_items.objects.filter(item_class='PRODUCT',item_type='PENCIL')

    return render(request, 'products/product_list.html',{'cart_items':cart_items})

def paper_list(request):
    cart_items=Cart_items.objects.filter(item_class='PRODUCT',item_type='PAPER')
    
    return render(request, 'products/product_list.html',{'cart_items':cart_items})
    



    
    
         
        
        
    
    
