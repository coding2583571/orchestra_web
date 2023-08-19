from django.db import models

class Contact(models.Model):
    first_name = models.CharField(blank=True, max_length=500)
    last_name = models.CharField(blank=True, max_length=500)
    job_title = models.CharField(blank=True, max_length=500)
    work_number = models.CharField(blank=True, max_length=500)
    alternate_number = models.CharField(blank=True, max_length=500)
    work_email = models.CharField(blank=True, max_length=500)
    alternate_email = models.CharField(blank=True, max_length=500)
    work_address = models.TextField(blank=True, max_length=500)

# Create your models here.
