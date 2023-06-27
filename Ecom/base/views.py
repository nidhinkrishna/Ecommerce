from django.shortcuts import render,HttpResponse
from store.models import Products,ReviewRating

# Create your views here.
def home(request):

    trending = Products.objects.all().filter(is_available = True).order_by('-created_date')

    for trend in trending:
        reviews = ReviewRating.objects.filter(product_id=trend.id, status=True)

    context = {
        'trending':trending,
        'reviews':reviews
    }

    return render (request,'base/home.html',context)
