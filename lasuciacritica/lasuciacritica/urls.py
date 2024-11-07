"""lasuciacritica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from criticas import views
from django.conf import settings



urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home, name='home'),
  path('accion_aventura/', views.accion_aventura, name='accion_aventura'),
  path('comedia/', views.comedia, name='comedia'),
  path('drama/', views.drama, name='drama'),
  path('ciencia_fantasia/', views.ciencia_fantasia, name='ciencia_fantasia'),
  path('horror_suspenso/', views.horror_suspenso, name='horror_suspenso'),
  path('romance/', views.romance, name='romance'),
  path('animacion/', views.animacion, name='animacion'),
  path('documental/', views.documental, name='documental'),
  path('blog/', views.blog, name='blog'),
  path('pelicula_detalles/<int:pelicula_id>/', views.pelicula_detalles, name="pelicula_detalles"),

]
    
if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)