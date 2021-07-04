from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Clothe, Textile, Photo 
from .forms import AccessorizingForm

from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'kayenneclothes'

# view functions 

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def clothes_index(request):
    clothes = Clothe.objects.filter(user=request.user)
    return render(request, 'clothes/index.html', { 'clothes': clothes })

@login_required
def clothes_detail(request, clothe_id):
    clothe = Clothe.objects.get(id=clothe_id)
    # return render(request, 'clothes/detail.html', { 'clothe': clothe })
    textiles_clothe_doesnt_have = Textile.objects.exclude(id__in = clothe.textiles.all().values_list('id'))
    accessorizing_form = AccessorizingForm()
    return render(request, 'clothes/detail.html', { 'clothe': clothe, 'accessorizing_form': accessorizing_form, 'textiles': textiles_clothe_doesnt_have
    })

@login_required
def add_accessorizing(request, clothe_id):
    form = AccessorizingForm(request.POST)
    if form.is_valid():
        new_accessorizing = form.save(commit=False)
        new_accessorizing.clothe_id = clothe_id
        new_accessorizing.save()
    return redirect('detail', clothe_id=clothe_id)

@login_required
def assoc_textile(request, clothe_id, textile_id):
    Clothe.objects.get(id=clothe_id).textiles.add(textile_id)
    return redirect('detail', clothe_id=clothe_id) 

@login_required
def unassoc_textile(request, clothe_id, textile_id):
    Clothe.objects.get(id=clothe_id).textiles.remove(textile_id)
    return redirect('detail', clothe_id=clothe_id)

@login_required
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

class ClotheCreate(LoginRequiredMixin, CreateView):
    model = Clothe
    fields = ['name', 'productcat', 'description', 'size']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class ClotheUpdate(LoginRequiredMixin, UpdateView):
    model = Clothe
    fields = ['productcat', 'description', 'size']

class ClotheDelete(LoginRequiredMixin, DeleteView):
    model = Clothe
    success_url = '/clothes/'

class TextileList(LoginRequiredMixin, ListView):
    model = Textile

class TextileDetail(LoginRequiredMixin, DetailView): 
    model = Textile 

class TextileCreate(LoginRequiredMixin, CreateView):
    model = Textile
    fields = '__all__'

class TextileUpdate(LoginRequiredMixin, UpdateView):
    model = Textile
    fields = ['name', 'color']

class TextileDelete(LoginRequiredMixin, DeleteView): 
    model = Textile
    success_url = '/textiles/'