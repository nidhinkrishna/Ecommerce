from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from brands.models import Brands
from . models import *
from cart.models import CartItem
from cart.views import _cart_id
from django.db.models import Q
# paginator 
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def store(request,brands_slug = None):
    brands = None
    products = None
    if brands_slug != None:
        brands = get_object_or_404(Brands,slug=brands_slug)
        products = Products.objects.filter(brand_name = brands,is_available = True).order_by('id')
        paginator = Paginator(products,6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    else:
        products= Products.objects.all()
        paginator = Paginator(products,6)
        page =request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()

    context = {
        'products':paged_products,
        'count':products_count
    
    }
    

    return render (request,'store/store.html',context)

def fetch_products_by_price(request,min_price,max_price):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price == '' or max_price == '':
        return redirect('store')
    
        
        
    
    products = Products.objects.filter(selling_price__gte=min_price, selling_price__lte=max_price ) 
 
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
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product = single_product).exists()
    except Exception as e:
        raise e
    
    context = {
        'single_product':single_product,
        'in_cart' :in_cart
    }

    return render (request,'store/product_detail.html',context)


def search(request):
    context  = {}
    products = None
    products_count = None
    if request.method == 'GET':
        query = request.GET.get('Keyword')

        if query != '':
            products = Products.objects.order_by('-created_date').filter(Q(products_description__icontains=query)|Q(product_name__icontains=query))
            products_count = products.count()
        else:
            return redirect('store')
            
    context = {
        'products':products,
        'count':products_count
    }
    return render(request,'store/store.html',context)
