from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Clothe

# view functions 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def clothes_index(request):
    clothes = Clothe.objects.all()
    return render(request, 'clothes/index.html', { 'clothes': clothes })

def clothes_detail(request, clothe_id):
    clothe = Clothe.objects.get(id=clothe_id)
    return render(request, 'clothes/detail.html', { 'clothe': clothe })

class ClotheCreate(CreateView):
    model = Clothe
    fields = '__all__'
    success_url = '/clothes/'

class ClotheUpdate(UpdateView):
    model = Clothe
    fields = ['product', 'description', 'size']

class ClotheDelete(DeleteView):
    model = Clothe
    success_url = '/clothes/'