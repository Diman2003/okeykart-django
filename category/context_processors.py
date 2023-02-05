from .models import Category

def manu_links(request):
    links = Category.objects.all()
    
    return dict(links=links)