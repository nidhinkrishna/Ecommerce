from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.cart,name='cart'),
    path('add_cart/<product_id>/',views.add_cart,name='add_cart'),
    path('decrement_cart/<product_id>/<int:cart_item_id>/',views.decrement_cart,name='decrement_cart'),
    path('remove_item/<product_id>/<int:cart_item_id>/',views.remove_item,name='remove_item'),
    path('checkout/',views.checkout,name='checkout')
    
]
