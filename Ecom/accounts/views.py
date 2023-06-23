from django.shortcuts import render,redirect
from . forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          
           form.save()
           return redirect('login')

    return render(request,'accounts/register.html',{'form':form})

def loginfunc(request):

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        
        
        user=authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
        
            return redirect('store')

    return render(request,'accounts/login.html')

def logoutfunc(request):

    pass