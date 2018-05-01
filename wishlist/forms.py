from django import forms
from .models import Wishlist



        
class WishlistForm(forms.ModelForm):
    
    class Meta:
        model=Wishlist
        exclude = ('user','product_id')
        
        