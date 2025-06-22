# UAS/jadwal_dosen/jadwal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking_kelas, name='booking_kelas'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('export/', views.export_excel, name='export_excel'),
]