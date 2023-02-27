from django.db import models
from datetime import datetime
from django.urls import reverse


# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=200 , default='')
    created_at = models.DateTimeField(default=datetime.now(),blank=True)
    created_by = models.CharField(default='amit',max_length=200)

    def get_absolute_url(self):
        return reverse('retrive',kwargs={'pk':self.pk})


class projects(models.Model):
    
    project_name = models.CharField(max_length=200)
