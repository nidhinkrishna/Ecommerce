from django.contrib import admin
from . models import *
# Register your models here.
class CartDisplay(admin.ModelAdmin):
    list_display = ('cart_id','date_added')
admin.site.register(Cart,CartDisplay)
class CartItemDisplay(admin.ModelAdmin):
    list_display = ('product','cart','quantity','is_active')
admin.site.register(CartItem,CartItemDisplay)