from django.shortcuts import render
from django.http import HttpResponse

def alamat_view(request):
    return HttpResponse("Alamat: Jl. KH. Mama Oyon No. 11, Cicantayan Sukabumi")

def telepon_view(request):
    return HttpResponse("Telepon: +62 838-0604-5240")