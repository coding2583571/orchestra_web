from django.contrib import admin
from .models import Title

class TitleAdmin(admin.ModelAdmin):
    list_display = ('Title','Date')

admin.site.register(Title, TitleAdmin)

# Register your models here.
