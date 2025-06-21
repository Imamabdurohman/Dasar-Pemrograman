from django.urls import path
from . import views

urlpatterns = [
    path('hasil/', views.show_results, name='polls-results'),
]
