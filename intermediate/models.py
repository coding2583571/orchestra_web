from django.db import models

class Director(models.Model):
    Name = models.CharField(max_length=1050, blank=True)
    Email = models.EmailField(max_length=500, blank=True)
    Phone = models.CharField(max_length=20, blank=True)

class Concert(models.Model):
    concert_name = models.CharField(max_length=1050, blank=True)
    concert_date_and_time = models.DateTimeField(blank=True)
    location_address = models.TextField(blank=True, max_length=5000)
    notes = models.TextField(blank=True, max_length=5000)
    #add one for directors
    Qualifying_Orchestras = models.TextField(blank=True,help_text='Which orchestras are involved/playing in this concert?', max_length=5000)
    Director_In_Charge = models.ForeignKey(Director, on_delete=models.CASCADE)


class Contest(models.Model):
    contest_name = models.CharField(max_length=1050, blank=True)
    contest_date_and_time = models.DateTimeField(blank=True)
    location_address = models.TextField(blank=True, max_length=5000)
    notes = models.TextField(blank=True, max_length=5000)
    #add one for directors
    Qualifying_Orchestras = models.TextField(blank=True,help_text='Which orchestras are involved/playing in this concert?', max_length=5000)
    # want to modify qualifying orchestra all three models - more like option based
    Director_In_Charge = models.ForeignKey(Director, on_delete=models.CASCADE)


class Event(models.Model):
    event_name = models.CharField(max_length=1050, blank=True)
    event_date_and_time = models.DateTimeField(blank=True)
    location_address = models.TextField(blank=True, max_length=5000)
    notes = models.TextField(blank=True, max_length=5000)
    #add one for directors
    Qualifying_Orchestras = models.TextField(blank=True,help_text='Which orchestras are involved/playing in this concert?', max_length=5000)
    Director_In_Charge = models.ForeignKey(Director, on_delete=models.CASCADE)

# Create your models here.
