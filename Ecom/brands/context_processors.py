from .models import Brands

def menu_links(request):
    links = Brands.objects.all()
    
    return {"links":links}