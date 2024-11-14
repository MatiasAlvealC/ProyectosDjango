from django.shortcuts import render, get_object_or_404
from .models import Clasificacion, Post

# Create your views here.
def blog(request):
  post = Post.objects.all()
  category = Clasificacion.objects.all()
  return render(request, "shop/blog.html", {'post':post, 'category':category})   

def category(request, category_id):
  #categoria = Clasificacion.objects.get(id = category_id)
  categoria = get_object_or_404(Clasificacion, id = category_id)
  post = Post.objects.filter(classification = categoria)
  return render(request, "shop/category.html",
                {'post':post, 'category':categoria})