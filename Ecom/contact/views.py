from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.
def about(request):

    return render(request,'contact/about.html')

def contact(request):
    form = ContactForm
    # context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
      

        if form.is_valid():
            form.save()

            return redirect('contact')
        
   
      
    return render(request,'contact/contact.html',{'form':form})