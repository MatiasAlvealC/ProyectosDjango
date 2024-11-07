from django.shortcuts import render
from .models import Pelicula
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404

def home(request):
  peliculas = Pelicula.objects.all()
  paginator = Paginator(peliculas, 30)  # Show 3 galeries per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request, "criticas/home.html", {"page_obj": page_obj})

def accion_aventura(request):
  peliculas = Pelicula.objects.filter(Q(genero__icontains="Animación") | Q(genero__icontains="Acción"))
  paginator = Paginator(peliculas, 30)  
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)  
  return render(request, "criticas/accion_aventura.html", {"page_obj": page_obj})

def comedia(request):
  peliculas = Pelicula.objects.filter(genero__icontains="Comedia")
  paginator = Paginator(peliculas, 30)  # Show 3 galeries per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request,"criticas/comedia.html", {"page_obj": page_obj})

def drama(request):
  peliculas = Pelicula.objects.filter(genero__icontains="Drama")
  paginator = Paginator(peliculas, 30)  # Show 3 galeries per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request,"criticas/drama.html", {"page_obj": page_obj})

def ciencia_fantasia(request):
  peliculas = Pelicula.objects.filter(Q(genero__icontains="Ciencia Ficción") | Q(genero__icontains="Fantasía"))
  paginator = Paginator(peliculas, 30)  
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)  
  return render(request, "criticas/ciencia_fantasia.html", {"page_obj": page_obj})
  


def horror_suspenso(request):
  peliculas = Pelicula.objects.filter(Q(genero__icontains="Terror") | Q(genero__icontains="Suspenso"))
  paginator = Paginator(peliculas, 30)  
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)  
  return render(request,"criticas/horror_suspenso.html", {"page_obj": page_obj})

def romance(request):
  peliculas = Pelicula.objects.filter(genero__icontains="Romance")
  paginator = Paginator(peliculas, 30)  # Show 3 galeries per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request,"criticas/romance.html", {"page_obj": page_obj})

def animacion(request):
  peliculas = Pelicula.objects.filter(genero__icontains="Animación")
  paginator = Paginator(peliculas, 30)  # Show 3 galeries per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request, "criticas/animacion.html", {"page_obj": page_obj})

def documental(request):
  peliculas = Pelicula.objects.filter(genero__icontains="Documental")
  paginator = Paginator(peliculas, 30)  # Show 3 galeries per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request,"criticas/documental.html", {"page_obj": page_obj})

def blog(request):
  peliculas = Pelicula.objects.all()
  paginator = Paginator(peliculas, 12)  # Show 3 galeries per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request,"criticas/blog.html", {"page_obj": page_obj})

def pelicula_detalles(request, pelicula_id):
  pelicula = get_object_or_404(Pelicula, id=pelicula_id)
  return render(request, "criticas/pelicula_detalles.html", {"pelicula": pelicula})