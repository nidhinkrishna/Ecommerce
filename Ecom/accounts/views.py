from django.shortcuts import render,redirect
from . forms import RegistrationForm

# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          
           form.save()
           return redirect('login')

    return render(request,'accounts/register.html',{'form':form})

def login(request):

    return render(request,'accounts/login.html')

def logoutfunc(request):

    pass