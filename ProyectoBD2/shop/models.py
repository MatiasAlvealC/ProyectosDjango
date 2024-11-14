from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Clasificacion(models.Model):
  name = models.CharField(max_length = 100, verbose_name = "Nombre")
  created = models.DateTimeField(auto_now_add = True, verbose_name = "Fech. Creacion")
  updated = models.DateTimeField(auto_now_add = True, verbose_name = "Fech. Edicion")
  
  class Meta:
    verbose_name = "categoria"
    verbose_name_plural = "Categorias"
  
  def __str__(self):
    return (self.name)   
  
class Post(models.Model):
  title = models.CharField(max_length = 100, verbose_name = "Nombre Producto")
  content = models.TextField(verbose_name = "Descripcion")
  published = models.DateField(default = now, verbose_name = "Fech. Public")
  author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Autor")
  classification = models.ManyToManyField(Clasificacion, verbose_name = "Categoria")
  created = models.DateTimeField(auto_now_add = True, verbose_name = "Fech. Creacion")
  updated = models.DateTimeField(auto_now_add = True, verbose_name = "Fech. Edicion")
  
  class Meta:
    verbose_name = "Producto"
    verbose_name_plural = "Productos"
  
  def __str__(self):
    return (self.title)
