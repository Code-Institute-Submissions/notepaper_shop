from django.db import models

# Create your models here.
class Coupon(models.Model):
    name = models.CharField(max_length=254, default='' )
    code=models.CharField(max_length=7, default='')
    discount=models.DecimalField(max_digits=3, decimal_places=2)
    
    
    def __str__(self):
        return self.name
        
        
        
        
