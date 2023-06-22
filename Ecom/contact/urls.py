from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('about/',views.about,name='about'),
    path('',views.contact,name='contact')
]
