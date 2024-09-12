
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shopping/', views.shopping, name='shopping'),
    path('admin/', admin.site.urls),
]
