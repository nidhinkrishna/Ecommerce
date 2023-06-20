from django.urls import path
from . import views
from .views import store,fetch_products_by_price,product_detail
urlpatterns = [
    path('',views.store,name='store'),

    path('<slug:brands_slug>/',views.store,name='product_by_brand'),
    path('products/price/<int:min_price>/<int:max_price>/',views.fetch_products_by_price, name='fetch_products'),
    path('<slug:brands_slug>/<slug:products_slug>/',views.product_detail,name='product_detail'),
    
]
