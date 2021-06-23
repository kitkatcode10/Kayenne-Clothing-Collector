from django.forms import ModelForm
from .models import Accessorizing

class AccessorizingForm(ModelForm):
  class Meta:
    model = Accessorizing
    fields = ['date', 'accessory']