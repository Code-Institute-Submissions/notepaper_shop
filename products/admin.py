from django.contrib import admin
from products.models import Cart_items,Product,Coupon
# Register your models here.
admin.site.register(Cart_items)
admin.site.register(Product)
admin.site.register(Coupon)