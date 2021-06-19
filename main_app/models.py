from django.db import models
from django.urls import reverse 

# Create your models here.


ACCESORIES = (
  ('S', 'Shoes'),
  ('J', 'Jewellery'),
  ('H', 'Headwear'),
  ('B', 'Bag'), 
)

class Clothe(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'clothe_id': self.id})

class Accessorizing(models.Model): 
    date = models.DateField()
    accessory = models.CharField(
        max_length=250, 
        choices=ACCESORIES, 
        default=ACCESSORIES[0][0]   
    )
    
    clothe = models.ForeignKey(Clothe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_accessory_display()} on {self.date}"

  
