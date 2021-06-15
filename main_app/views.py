from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Clothe:
  def __init__(self, name, productcat, description, size):
    self.name = name
    self.productcat = productcat
    self.description = description
    self.size = size

clothes = [
  Clothe('The Kayenne Skort', 'Skirt', 'office skort', 'small'),
  Clothe('Zoom Sweater', 'Sweater', 'sweater with detachable collar', 'medium'),
  Clothe('Aperitif Tank', 'Tank Top - sleeveless top', 'frilly tank', 'small')
]


# view functions 

def home(request):
    return HttpResponse('<h1>CLOTHES!</h1>')

def about(request):
    return render(request, 'about.html')

def clothes_index(request):
    return render(request, 'clothes/index.html', { 'clothes': clothes })