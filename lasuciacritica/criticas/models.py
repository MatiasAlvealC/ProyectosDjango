from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    sinopsis = models.TextField()
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=255, help_text="Lista de géneros separados por comas")
    duracion = models.IntegerField(help_text="Duración en minutos")
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')  # Define un valor predeterminado
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "pelicula"
        verbose_name_plural = "peliculas"

    def __str__(self):
        return self.titulo
