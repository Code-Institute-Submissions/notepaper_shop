from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from products.models import Product
from cart.utils import get_cart_items_and_total
from coupon.forms import CouponForm
from coupon.models import Coupon
from decimal import *


def apply_coupon(request):
    coupon_code = request.POST['code']
    if Coupon.objects.filter(code=coupon_code).exists():
        coupon = Coupon.objects.get(code=request.POST['code'])
        request.session['discount'] = coupon.discount 
    else:
        request.session['discount'] = 0
    return redirect("view_cart")


# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', {})
    discount = request.session.get('discount', 0)

    context = get_cart_items_and_total(cart, discount)
    
    return render(request, "cart/view_cart.html", context)
        
        
def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('view_product',id)
    
def add_to_cart_product_list(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'),'view_product',id)   
    
    
    
    
    
    
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart')   

def update_quantity(request,id):
    quantity = int(request.POST.get('quantity',0))
    cart = request.session.get('cart', {})
    cart[id] =  quantity
    
    request.session['cart'] = cart   

    return redirect('view_cart')
    

    
    