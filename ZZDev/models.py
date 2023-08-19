from django.db import models

class Bootstrap(models.Model):
    CSS_Href = models.TextField()
    CSS_Integrity = models.TextField()

    CSS_Script_Source = models.TextField()
    CSS_Script_Integrity = models.TextField()

    JS_Script_1 = models.TextField()
    JS_Script_1_Integrity = models.TextField()

    JS_Script_2 = models.TextField()
    JS_Script_2_Integrity = models.TextField()

    Version = models.CharField(max_length=100,blank=True)
    Date_Updated = models.DateField(blank=True)

# Create your models here.
