from django.contrib import admin
from .models import Products,ReviewRating,ProductGallery
import admin_thumbnails

# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductsDisplay(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name','brand_name','actual_price','selling_price','ram','storage','stock','trending','is_available','created_date','connectivity')
    inlines = [ProductGalleryInline]
admin.site.register(Products,ProductsDisplay)
admin.site.register(ReviewRating)


admin.site.register(ProductGallery)