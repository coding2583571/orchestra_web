from django.contrib import admin
from .models import Title, Link

class TitleAdmin(admin.ModelAdmin):
    list_display = ('Title','Date')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('Name','HyperLink')

admin.site.register(Title, TitleAdmin)
admin.site.register(Link, LinkAdmin)


# Register your models here.
