# Generated by Django 4.1 on 2024-11-14 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fech. Creacion')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fech. Edicion')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nombre Producto')),
                ('content', models.TextField(verbose_name='Descripcion')),
                ('published', models.DateField(default=django.utils.timezone.now, verbose_name='Fech. Public')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fech. Creacion')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fech. Edicion')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('classification', models.ManyToManyField(to='shop.clasificacion', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]