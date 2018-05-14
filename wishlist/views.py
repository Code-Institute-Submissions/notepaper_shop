from django.shortcuts import render,get_object_or_404,redirect
from wishlist.models import Wishlist
from products.models import Product
from wishlist.forms import WishlistForm
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
 
def add_to_wishlist(request):
  response_data = {} 
  if not request.user.is_authenticated:
        return redirect('login')
        
  if request.method=='POST':
        form=WishlistForm(request.POST)
        if form.is_valid():
            list_item=form.save(commit=False)
            list_item.user=request.user
            list_item.product_id=request.POST['ids']
            list_item.save()
            
            return HttpResponse(status=204)
@login_required()      
def view_wishlist(request):
     
     list_item=Wishlist.objects.filter(user=request.user)
     return render(request, "wishlist/wishlist.html",{'list_item':list_item})
    
