from django.contrib import admin
from .models import Products,ReviewRating

# Register your models here.
class ProductsDisplay(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name','brand_name','actual_price','selling_price','ram','storage','stock','trending','is_available','created_date','connectivity')

admin.site.register(Products,ProductsDisplay)
admin.site.register(ReviewRating)