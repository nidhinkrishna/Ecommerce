from django.urls import path 
from .views import *
from . import views


urlpatterns = [
    path('place_order/',views.place_order,name='place_order')
]
