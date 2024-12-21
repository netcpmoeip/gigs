from django.shortcuts import render, get_object_or_404
from .models import Page, News, Leg
from datetime import datetime

# Create your views here.
def index(request):
    legs = Leg.objects.filter(departure__gte=datetime.now())
    news = News.objects.all().order_by('-created_at')[:3]
    shipyard = Page.objects.get(slug='shipyard')
    gigs = Page.objects.get(slug='gigs')
    return render(request, 'main/index.html', {'shipyard': shipyard, 'gigs': gigs, 'legs': legs, 'news': news} )

def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'main/page.html', {'page': page})

def news(request):
    articles = News.objects.all().order_by('-created_at')
    return render(request, 'main/news.html', {'news': articles})

def article(request, slug):
    article = get_object_or_404(News, slug=slug)
    return render(request, 'main/article.html', {'article': article})

def leg(request, id):
    leg = get_object_or_404(Leg, id=id)
    return render(request, 'main/leg.html', {'leg': leg})