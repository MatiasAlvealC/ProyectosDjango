from django.shortcuts import render
from .models import Galeria

def galeria(request):
    galerias = Galeria.objects.all()
    return render(request,"gallery/galeria.html", {'galerias':galerias})