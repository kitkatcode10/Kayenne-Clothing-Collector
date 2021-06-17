from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('clothes/', views.clothes_index, name='index'), 
    path('clothes/<int:clothe_id>/', views.clothes_detail, name='detail'),
    path('clothes/create/', views.ClotheCreate.as_view(), name='clothes_create'),
    path('clothes/<int:pk>/update/', views.ClotheUpdate.as_view(), name='clothes_update'), 
    path('clothes/<int:pk>/delete/', views.ClotheDelete.as_view(), name='clothes_delete'), 
]

