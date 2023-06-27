from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.models import Cart,CartItem
from cart.views import _cart_id
import requests
from orders.models import Order,OrderProduct



# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          
           form.save()
           messages.success(request,"Registration Successfull")

         
           return redirect('login')
        messages.error(request,'Invalid Data Try Again') 
    return render(request,'accounts/register.html',{'form':form})

def loginfunc(request):

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        
        
        user=authenticate(request,email=email,password=password)

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id = _cart_id(request))
                is_cart_items_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_items_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    for item in cart_item:
                        item.user = user
                        item.save()
               

            except:
                pass
            login(request,user)
            messages.success(request,'Login Succesfull')
            url = request.META.get('HTTP_REFERER')

            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                return redirect(nextPage)
            except:
                return redirect('dashboard')
        
           
        messages.error(request,"Invalid Login Credentials")
    

    return render(request,'accounts/login.html')

def logoutfunc(request):
    user=request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request,'Logout Success')

        return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()

    userprofile = UserProfile.objects.get(user_id=request.user.id)
    context = {
        'orders_count': orders_count,
        'userprofile': userprofile,
    }
    return render(request, 'accounts/dashboard.html', context)







@login_required(login_url='login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'accounts/my_orders.html', context)




@login_required(login_url='login')
def order_detail(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)
    subtotal = 0
    for i in order_detail:
        subtotal += i.product_price * i.quantity

    context = {
        'order_detail': order_detail,
        'order': order,
        'subtotal': subtotal,
    }
    return render(request, 'accounts/order_detail.html', context)