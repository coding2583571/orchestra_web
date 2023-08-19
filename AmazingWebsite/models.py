from django.db import models

class Heading(models.Model):
   Website_Title = models.CharField(max_length=1000, blank=True)
   Date = models.DateField(blank=True)
# Create your models here.
