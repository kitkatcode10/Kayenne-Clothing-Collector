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
    path('clothes/<int:clothe_id>/add_accessorizing/', views.add_accessorizing, name='add_accessorizing'),
    path('clothes/<int:clothe_id/add_photo/', views.add_photo, name='add_photo'), 
    path('clothes/<int:clothe_id>/assoc_textile/<int:textile_id>/', views.assoc_textile, name='assoc_textile'), 
    path('clothes/<int:clothe_id>/unassoc_textile/<int:textile_id>/', views.unassoc_textile, name='unassoc_textile'),
    path('textiles/', views.TextileList.as_view(), name='textiles_index'),
    path('textiles/<int:pk>/', views.TextileDetail.as_view(), name='textiles_detail'),
    path('textiles/create/', views.TextileCreate.as_view(), name='textiles_create'),
    path('textiles/<int:pk>/update/', views.TextileUpdate.as_view(), name='textiles_update'),
    path('textiles/<int:pk>/delete/', views.TextileDelete.as_view(), name='textiles_delete'),
]

