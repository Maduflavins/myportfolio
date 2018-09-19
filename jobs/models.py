from django.db import models

# Create your models here.

class Job(models.Model):
    Title = models.CharField(max_length=200, default="title")
    image = models.ImageField(upload_to='images/jobs/')
    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.Title
