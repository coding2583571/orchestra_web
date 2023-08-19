from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','job_title','work_number','work_email')


admin.site.register(Contact, ContactAdmin)

# Register your models here.
