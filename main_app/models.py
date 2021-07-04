from django.db import models
from django.urls import reverse 
from datetime import date 
# import the user
from django.contrib.auth.models import User

# Create your models here.


ACCESSORIES = (
  ('S', 'Shoes'),
  ('J', 'Jewellery'),
  ('H', 'Headwear'),
  ('B', 'Bag'), 
)

class Textile(models.Model): 
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('textiles_detail', kwargs={'pk': self.id}) 

class Clothe(models.Model):
    name = models.CharField(max_length=100)
    productcat = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)
    textiles = models.ManyToManyField(Textile) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'clothe_id': self.id})

    def accessorized_for_today(self): 
        return self.accessorizing_set.filter(date=date.today()).count() >=len(ACCESSORIES)

class Accessorizing(models.Model): 
    date = models.DateField('accessorizing date')
    accessory = models.CharField(
        max_length=250, 
        choices=ACCESSORIES, 
        default=ACCESSORIES[0][0]   
    )
    
    clothe = models.ForeignKey(Clothe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_accessory_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    clothe = models.ForeignKey(Clothe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for clothe_id: {self.clothe_id} @{self.url}" 
  

