from django.db import models
from brands.models import Brands

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(blank=True,unique=True)
    brand_name = models.ForeignKey(Brands,on_delete=models.CASCADE)
    products_description = models.TextField(blank=True)
    actual_price = models.IntegerField()
    selling_price = models.IntegerField()
    trending = models.BooleanField(default=False,help_text='1:show,0:hide')
    stock = models.IntegerField()
    product_image = models.ImageField(upload_to='photos/products')
    ram = models.CharField(max_length=10)
    storage = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    connectivity = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
    

    