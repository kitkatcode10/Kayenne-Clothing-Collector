from django.db import models
from django.urls import reverse 

# Create your models here.

class Clothe(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'clothe_id': self.id})

  
