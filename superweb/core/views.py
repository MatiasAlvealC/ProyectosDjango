from django.shortcuts import render, HttpResponse
"""
Esto es de la clase pasada
plantilla =
<h1> TITULIN </h1>
<hr>
<ul>
    <li><a href='/'>Inicio</a></li>
    <li><a href='/gallery/'>Galeria</a></li>
    <li><a href='/faq/'>Preguntas</a></li>
</ul>
def home(request):
    return HttpResponse(plantilla+"<p>Soy el inicio<p>")

def gallery(request):
    return HttpResponse(plantilla+"<p>Soy una galeria<p>")

def faq(request):
    return HttpResponse(plantilla+"<p>Soy la seccion de preguntas frecuente<p>")
"""

def home(request):
    return render(request,"core/home.html")
def gallery(request):
    return render(request,"core/gallery.html")
def faq(request):
    return render(request,"core/faq.html")