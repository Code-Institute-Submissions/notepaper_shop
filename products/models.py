from django.db import models
from model_utils.managers import InheritanceManager


# Create your models here.


class Cart_items(models.Model):
    PEN = 'PEN'
    PENCIL = 'PENCIL'
    PAPER = 'PAPER'
    
    COUPON ='COUPON'
    PRODUCT = 'PRODUCT'
    
    TYPE_CHOICES=((PEN, 'pen'),
        (PENCIL, 'pencil'),
         (PAPER, 'paper'),
         (COUPON, 'coupon')
        )
    CLASS_CHOICES=((COUPON, 'coupon'),
        (PRODUCT, 'product'),
     
        )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    item_type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
        default=PEN,
    )
    item_class=models.CharField(
        max_length=7,
        choices=CLASS_CHOICES,
        default=PRODUCT,
    )
    objects = InheritanceManager()

    def __str__(self):
        return self.name
        
class Product(models.Model):
    cart_items = models.OneToOneField(
        Cart_items,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    

    def __str__(self):
        return self.cart_items.name
        
class Coupon(models.Model):
    cart_items = models.OneToOneField(
        Cart_items,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    code = models.CharField(max_length=7, default='')
    discount = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.cart_items.name
        
        