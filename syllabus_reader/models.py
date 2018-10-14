from django.db import models


# Create your models here.
class History(models.Model):  # DELETE THIS
    # my db model
    url = models.CharField(max_length=200)
    data = models.CharField(max_length=2500)
