from django.shortcuts import render

def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def products(request):
    return render(request,"core/products.html")

def blog(request):
    return render(request,"core/blog.html")

def contact(request):
    return render(request,"core/contact.html")