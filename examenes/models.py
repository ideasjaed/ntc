from django.db import models

# Create your models here.




class Examen(models.Model):
	TIPO_EXAMEN = (
        ('MM', 'MMPI-II'),
        ('GD', 'Gordon'),
        ('MS', 'Moss'),
        ('TM', 'Terman Meril'),
    )
	nombre = models.CharField(max_length=50,blank=True)
	descripcion = models.TextField(blank=True)
	tipo_examen = models.CharField(max_length=1, choices=TIPO_EXAMEN)



class Preguntas(models.Model):
	pregunta = models.CharField(max_length=70)
	respuesta = models.CharField(max_length=10)
	
