from django.db import models

class Title(models.Model):
   Title = models.CharField(max_length=1000, blank=True)
   Date = models.DateField(blank=True)

class Link(models.Model):
   Name = models.CharField(max_length=5000, blank=True)
   HyperLink = models.CharField(max_length=5000, blank=True)
   #Date = models.DateField(blank=True)

# Create your models here.
