from django.shortcuts import render,HttpResponse
from store.models import Products

# Create your views here.
def home(request):

    trending = Products.objects.all().filter(is_available = True)

    context = {
        'trending':trending
    }

    return render (request,'base/home.html',context)
