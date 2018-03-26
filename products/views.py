from django.shortcuts import render,get_object_or_404,redirect
from products.models import Product
from .forms import ProductForm
from .models import Product

# Create your views here.
def pens_list(request):
    products=Product.objects.filter(item_type='PEN')
    
    return render(request, 'products/product_list.html',{'products':products})

def pencils_list(request):
    products=Product.objects.filter(item_type='PENCIL')

    return render(request, 'products/product_list.html',{'products':products})

def paper_list(request):
    products=Product.objects.filter(item_type='PAPER')
    
    return render(request, 'products/product_list.html',{'products':products})
    
def new_product(request):
    print("*****")
    print(request.method)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
     
        if form.is_valid():
            products=form.save(commit=False)
            
           
            products.save()
           
            
            
            return redirect('home')
    else:
        
        form=ProductForm()
    return render(request, 'products/new_product.html',{'form':form})
    



    
    
         
        
        
    
    
