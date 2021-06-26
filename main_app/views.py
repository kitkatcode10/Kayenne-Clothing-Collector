from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import AccessorizingForm

import uuid
import boto3
from .models import Clothe, Textile, Photo 

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'kayenneclothes'

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
    # return render(request, 'clothes/detail.html', { 'clothe': clothe })
    textiles_clothe_doesnt_have = Textile.objects.exclude(id__in = clothe.textiles.all().values_list('id'))
    accessorizing_form = AccessorizingForm()
    return render(request, 'clothes/detail.html', { 'clothe': clothe, 'accessorizing_form': accessorizing_form, 'textiles': textiles_clothe_doesnt_have
    })

def add_accessorizing(request, clothe_id):
    form = AccessorizingForm(request.POST)
    if form.is_valid():
        new_accessorizing = form.save(commit=False)
        new_accessorizing.clothe_id = clothe_id
        new_accessorizing.save()
    return redirect('detail', clothe_id=clothe_id)

def assoc_textile(request, clothe_id, textile_id):
    Clothe.objects.get(id=clothe_id).textiles.add(textile_id)
    return redirect('detail', clothe_id=clothe_id) 

def unassoc_textile(request, clothe_id, textile_id):
    Clothe.objects.get(id=clothe_id).textiles.remove(textile_id)
    return redirect('detail', clothe_id=clothe_id)

def add_photo(request, clothe_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file: 
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try: 
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, clothe_id=clothe_id)
            photo.save()
        except: 
            print('An error occured uploading file to S3')
    return redirect('detail', clothe_id=clothe_id)

class ClotheCreate(CreateView):
    model = Clothe
    fields = ['name', 'productcat', 'description', 'size']

class ClotheUpdate(UpdateView):
    model = Clothe
    fields = ['productcat', 'description', 'size']

class ClotheDelete(DeleteView):
    model = Clothe
    success_url = '/clothes/'

class TextileList(ListView):
    model = Textile

class TextileDetail(DetailView): 
    model = Textile 

class TextileCreate(CreateView):
    model = Textile
    fields = '__all__'

class TextileUpdate(UpdateView):
    model = Textile
    fields = ['name', 'color']

class TextileDelete(DeleteView): 
    model = Textile
    success_url = '/textiles/'