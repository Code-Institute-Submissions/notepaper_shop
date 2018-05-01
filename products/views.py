from django.shortcuts import render,get_object_or_404,redirect
from products.models import Product
from .forms import ProductForm
from .models import Product
from reviews.forms import ReviewForm
from wishlist.forms import WishlistForm

# Create your views here.
def products_list(request):
    products=Product.objects.all()
    product_count=products.count()
    
    form3=WishlistForm()
    if request.method=='GET' and 'filter' in request.GET:
        filters = request.GET['filter']
        if filters is not None and filters != '':
           
            filters = request.GET.get('filter', 'item_type')
            order = request.GET.get('order', 'price')
            products = products.filter(item_type=filters).order_by(order)
            
        return render(request, 'products/product_list.html', {
            'products': products,'product_count':product_count ,'item_type':filters,'wishlist_form':form3 })
    else:
        return render(request,'products/product_list.html',{
            'products':products,'product_count':product_count,'wishlist_form':form3
        })
        
def new_product(request):
   
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
     
        if form.is_valid():
            products=form.save(commit=False)
            
           
            products.save()
           
            
            
            return redirect('home')
    else:
        
        form=ProductForm()
    return render(request, 'products/new_product.html',{'form':form})
    

def view_product(request,id):
    products = get_object_or_404(Product, pk=id)
    form = ReviewForm()
    form2=WishlistForm()
    return render(request, "products/view_product.html", {'products': products,'review_form':form,'wishlist_form':form2})
    
def search_products(request):
    match = request.GET.get('match')
    
    if match=='contains':
        products = Product.objects.filter(name__icontains=request.GET['query'])
    else:
        products = Product.objects.filter(name__startswith=request.GET['query'])
    
    return render(request, "products/product_list.html", {"products": products})    
    

    

    
    
         
        
        
    
    
