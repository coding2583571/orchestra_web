from django.shortcuts import render
from AmazingWebsite.models import Title, Link
from ZZDev.models import Bootstrap

def web_homepage(request):
    website_title = Title.objects.all()
    bootstrap = Bootstrap.objects.all()
    links = Link.objects.all()
    return render(request, 'AmazingWebsite/web_homepage.html', {'website_title':website_title,'bootstrap':bootstrap,'links':links})

def contact(request):
    website_title = Title.objects.all()

    return render(request, 'contact/contact.html',{'website_title':website_title})

def high(request):
    website_title = Title.objects.all()

    return render(request, 'high/high.html',{'website_title':website_title})

def middle(request):
    website_title = Title.objects.all()

    return render(request, 'middle/middle.html',{'website_title':website_title})

def intermediate(request):
    website_title = Title.objects.all()

    return render(request, 'intermediate/intermediate.html',{'website_title':website_title})

def dev_panel(request):
    website_title = Title.objects.all()

    return render(request, 'ZZDev/dev_panel.html',{'website_title':website_title})

# Create your views here.
