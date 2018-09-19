from django.db import models
import datetime

# Create your models here.

class Technologies(models.Model):
    Title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/technologies/')
