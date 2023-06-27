from django.db import models
from brands.models import Brands
from django.urls import reverse

from django.db.models import Avg,Count
from accounts.models import Account


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

    def get_url(self):
        return reverse('product_detail', args=[self.brand_name.slug,self.slug])
    
    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
    

class ReviewRating(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    
class ProductGallery(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,default=None)
    image = models.ImageField(upload_to='store/products',max_length=255)

    def __str__(self):
        return self.product.product_name
    
    class Meta:
        verbose_name = 'ProductGallery'
        verbose_name_plural = 'ProductGallery'