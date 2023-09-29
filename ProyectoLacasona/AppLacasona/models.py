from django.db import models

# Create your models here.

class Newsletter(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class SendSong(models.Model):
    songname = models.CharField(max_length=30)
    email = models.EmailField(default="correo@ejemplo.com")
    url = models.URLField(default="https://ejemplo.com")
#    deadline = models.DateField()

class AskAnything(models.Model):
    message = models.CharField(max_length=100)
    email = models.EmailField(default="correo@ejemplo.com")