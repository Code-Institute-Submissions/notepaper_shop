from django.shortcuts import render,get_object_or_404,redirect
from products.models import Product
from .forms import ProductForm
from .models import Product

# Create your views here.
def pens_list(request):
    products=Product.objects.filter(item_type='PEN')
    
    return render(request, 'products/product_list.html',{'products':products,'item_type':'Pens','order_newest_latest':'pens_list','order_low_high':'pens_list_low','order_high_low':'pens_list_high'})

def pens_list_low(request):
    products=Product.objects.filter(item_type='PEN').order_by('price')

    return render(request, 'products/product_list.html',{'products':products,'item_type':'Pens','order_newest_latest':'pens_list','order_low_high':'pens_list_low','order_high_low':'pens_list_high'})

def pens_list_high(request):
    products=Product.objects.filter(item_type='PEN').order_by('price').reverse()
    
    return render(request, 'products/product_list.html',{'products':products,'item_type':'Pens','order_newest_latest':'pens_list','order_low_high':'pens_list_low','order_high_low':'pens_list_high'})

def pencils_list(request):
    products=Product.objects.filter(item_type='PENCIL')

    return render(request, 'products/product_list.html',{'products':products,'item_type':'Pencil','order_newest_latest':'pencils_list','order_low_high':'pencils_list_low','order_high_low':'pencils_list_high'})
    
def pencils_list_low(request):
    products=Product.objects.filter(item_type='PENCIL').order_by('price')

    return render(request, 'products/product_list.html',{'products':products,'item_type':'Pencil','order_newest_latest':'pencils_list','order_low_high':'pencils_list_low','order_high_low':'pencils_list_high'})

def pencils_list_high(request):
    products=Product.objects.filter(item_type='PENCIL').order_by('price').reverse()

    return render(request, 'products/product_list.html',{'products':products,'item_type':'Pencil','order_newest_latest':'pencils_list','order_low_high':'pencils_list_low','order_high_low':'pencils_list_high'})

def paper_list(request):
    products=Product.objects.filter(item_type='PAPER')
    
    return render(request, 'products/product_list.html',{'products':products,'item_type':'Paper','order_newest_latest':'paper_list','order_low_high':'paper_list_low','order_high_low':'paper_list_high'})
    



def paper_list_low(request):
    products=Product.objects.filter(item_type='PAPER').order_by('price')
    
    return render(request, 'products/product_list.html',{'products':products,'item_type':'Paper','order_newest_latest':'paper_list','order_low_high':'paper_list_low','order_high_low':'paper_list_high'})
    


def paper_list_high(request):
    products=Product.objects.filter(item_type='PAPER').order_by('price').reverse()
    
    return render(request, 'products/product_list.html',{'products':products,'item_type':'Paper','order_newest_latest':'paper_list','order_low_high':'paper_list_low','order_high_low':'paper_list_high'})
    
def product_list(request):
    products=Product.objects.all()
    
    return render(request, 'products/product_list.html',{'products':products,'item_type':'Products','order_newest_latest':'product_list','order_low_high':'product_list_low','order_high_low':'product_list_high'})
    
def product_list_low(request):
    products=Product.objects.all()
    
    return render(request, 'products/product_list.html',{'products':products,'item_type':'Products','order_newest_latest':'product_list','order_low_high':'product_list_low','order_high_low':'product_list_high'})
    
def product_list_high(request):
    products=Product.objects.all()
    
    return render(request, 'products/product_list.html',{'products':products,'item_type':'Products','order_newest_latest':'product_list','order_low_high':'product_list_low','order_high_low':'product_list_high'})

    
    
    
    
    
    
    

    

    
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
    

def view_product(request,id):
    products = get_object_or_404(Product, pk=id)
    
    return render(request, "products/view_product.html", {'products': products})
    
    
    

    

    
    
         
        
        
    
    
