from django.db import models
from store.models import Products

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=255,blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.selling_price * self.quantity

    def __str__(self):
        return self.product.product_name
    
   


