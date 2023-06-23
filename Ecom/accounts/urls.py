from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.loginfunc,name='login'),
    path('logout/',views.logoutfunc,name='logout'),
    
]
