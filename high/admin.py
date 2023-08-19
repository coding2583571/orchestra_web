from django.contrib import admin
from .models import Concert, Contest, Event
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('concert_name', 'concert_date_and_time', 'Qualifying_Orchestras')

class ContestAdmin(admin.ModelAdmin):
    list_display = ('contest_name','contest_date_and_time','Qualifying_Orchestras')

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_date_and_time','Qualifying_Orchestras')

# Register your models here.
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Event, EventAdmin)
