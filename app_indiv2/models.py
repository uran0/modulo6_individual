from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=70)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    

class Miembros(models.Model):
    nombre = models.CharField(max_length=70)
    apodo = models.CharField(max_length=20)
    edad = models.IntegerField()
    color_favorito = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
