from django import forms
from .models import Cart_items,Coupon



class Cart_itemsForm(forms.ModelForm):
    
    class Meta:
        model=Cart_items
        fields=('name','description','price','image','item_type',)
        
        

class CouponForm(forms.ModelForm):
    
    class Meta:
        model=Coupon
        
        fields=('discount','code')
    