from django.db import models

class Galeria(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title
