from django.contrib import admin
from .models import Clasificacion, Post


class ClasificationAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  
admin.site.register(Clasificacion, ClasificationAdmin)
admin.site.register(Post, PostAdmin)