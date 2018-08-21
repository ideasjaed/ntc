"""Users models"""

#Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Usuarios(models.Model):
	nombre = models.CharField(max_length=50,blank=True)
	apellidos = models.CharField(max_length=50,blank=True)
	direccion = models.TextField(blank=True,null=True)
	ocupacion = models.CharField(max_length=50,blank=True)
	edad = models.CharField(max_length=3,blank=True)
	estado_civil = models.CharField(max_length=20,blank=True)
	email = models.CharField(max_length=50,blank=True) 
	created = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.nombre

