from django.contrib import admin
from .models import Heading

class WebsiteTitleAdmin(admin.ModelAdmin):
    list_display = ('Website_Title','Date')

admin.site.register(Heading, WebsiteTitleAdmin)

# Register your models here.
