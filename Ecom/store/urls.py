from django.urls import path
from . import views
from .views import store
urlpatterns = [
    path('',views.store,name='store')
    
]
