from django.shortcuts import render,redirect
from . forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.models import Cart,CartItem
from cart.views import _cart_id


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


    return render(request,'accounts/dashboard.html')