from django.db import models
from django.utils import timezone



# Create your models here.
class Product(models.Model):
    PEN = 'PEN'
    PENCIL = 'PENCIL'
    PAPER = 'PAPER'
    
    TYPE_CHOICES=((PEN, 'pen'),
        (PENCIL, 'pencil'),
         (PAPER, 'paper'),
        
        )
 
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created_date = models.DateTimeField(auto_now_add=True)
    item_type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
        default=PEN,
    )
    
    

    def __str__(self):
        return self.name
        
        
        
        



        