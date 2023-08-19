from django.shortcuts import render
from AmazingWebsite.models import Title
from ZZDev.models import Bootstrap

def web_homepage(request):
    website_title = Title.objects.all()
    bootstrap = Bootstrap.objects.all()
    return render(request, 'AmazingWebsite/web_homepage.html', {'website_title':website_title,'bootstrap':bootstrap})

def contact(request):
    return render(request, 'contact/contact.html')

def high(request):
    return render(request, 'high/high.html')

def middle(request):
    return render(request, 'middle/middle.html')

def intermediate(request):
    return render(request, 'intermediate/intermediate.html')

def dev_panel(request):
    return render(request, 'ZZDev/dev_panel.html')

# Create your views here.
