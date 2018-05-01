from django.db import models
from products.models import Product
# Create your models here.


class Wishlist(models.Model):
     user = models.ForeignKey('auth.User', blank=False)
     product_id = models.IntegerField(default=0)
     