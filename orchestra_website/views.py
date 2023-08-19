from django.shortcuts import render
from AmazingWebsite.models import Title
from ZZDev.models import Bootstrap

def web_homepage(request):
    website_title = Title.objects.all()
    bootstrap = Bootstrap.objects.all()
    return render(request, 'AmazingWebsite/web_homepage.html', {'website_title':website_title,'bootstrap':bootstrap})

# Create your views here.
