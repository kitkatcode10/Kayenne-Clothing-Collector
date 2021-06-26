from django.contrib import admin
# import your models here
from .models import Clothe, Accessorizing, Textile, Photo

# Register your models here
admin.site.register(Clothe)
admin.site.register(Accessorizing)
admin.site.register(Textile)
admin.site.register(Photo)
