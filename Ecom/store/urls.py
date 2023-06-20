from django.urls import path
from . import views
from .views import store
urlpatterns = [
    path('',views.store,name='store'),
    path('store.html',views.store,name='store'),
    path('<slug:brands_slug>/',views.store,name='product_by_brand'),
    
]
