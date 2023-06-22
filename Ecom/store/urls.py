from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',views.store,name='store'),

    path('categories/<slug:brands_slug>/',views.store,name='product_by_brand'),
    path('products/price/<int:min_price>/<int:max_price>/',views.fetch_products_by_price, name='fetch_products'),
    path('categories/<slug:brands_slug>/<slug:products_slug>/',views.product_detail,name='product_detail'),
    path('search/',views.search,name='search')
    
]
