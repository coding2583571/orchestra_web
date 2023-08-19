from django.contrib import admin

from .models import Bootstrap

class BootstrapAdmin(admin.ModelAdmin):
    list_display = ('Version','Date_Updated')

admin.site.register(Bootstrap, BootstrapAdmin)

# Register your models here.
