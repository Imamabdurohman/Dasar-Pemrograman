from django.shortcuts import render
from django.http import HttpResponse

def alamat_view(request):
    return HttpResponse("Alamat: Jl. Simpang Dago No. 17, Jampang Kulon")

def telepon_view(request):
    return HttpResponse("Telepon: +62 857-2132-9929")