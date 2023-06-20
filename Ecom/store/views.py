from django.shortcuts import render,get_object_or_404,redirect
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

def fetch_products_by_price(request,min_price,max_price):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price == '' and max_price == '' :
        return redirect('store')
    
    products = Products.objects.filter(selling_price__gte=min_price, selling_price__lte=max_price)
    products_count = products.count()
    context = {
        'products': products,
        'min_price':min_price,
        'max_price':max_price,
        'count' :products_count
    }
    
    return render(request, 'store/product_list.html', context)


def product_detail(request,brands_slug,products_slug):
    try:
        single_product = Products.objects.get(brand_name__slug=brands_slug,slug=products_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product':single_product
    }

    return render (request,'store/product_detail.html',context)