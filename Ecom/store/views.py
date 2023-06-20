from django.shortcuts import render,get_object_or_404
from brands.models import Brands
from . models import *

# Create your views here.
def store(request,brands_slug = None):
    brands = None
    products = None
    if brands_slug != None:
        brands = get_object_or_404(Brands,slug=brands_slug)
        products = Products.objects.filter(brand_name = brands,is_available = True)
        products_count = products.count()
    else:
        products= Products.objects.all()
        products_count = products.count()

    context = {
        'products':products,
        'count':products_count
    
    }
    

    return render (request,'store/store.html',context)