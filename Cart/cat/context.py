from .models import cat

def links(request):
    link = cat.objects.all()
    return dict(link=link)

