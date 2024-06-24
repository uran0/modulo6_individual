from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=70)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    

class Miembros(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=70)
    apodo = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=120, default='contraseña')
    edad = models.IntegerField()
    color_favorito = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
