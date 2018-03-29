from django.test import TestCase,RequestFactory
from .views import *
from .models import Product
from django.contrib.auth.models import AnonymousUser, User

# Create your tests here.
class ProductViewTests(TestCase):
    def test_product_list_template(self):
        response=self.client.get('/products/products_list/')
        self.assertTemplateUsed(response, 'products/product_list.html')
        
        
    def test_view_product_that_exists(self):
        product=Product(
            name="Test Name",
            description="Test Description",
            price="3.00")
        product.save()
            
        response = self.client.get('/products/view_product/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/view_product.html")    
            
            
          