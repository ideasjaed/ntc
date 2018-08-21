from django.db import models

# Create your models here.

class PreguntaMMPI(models.Model):
	descripcion = models.CharField(max_length=70)

# class PregntasGordon(models.Model):
class PreguntaTM(models.Model):
	descripcion = models.CharField(max_length=150)

class RespuestaTM(models.Model):
	pregunta = models.ForeignKey(PreguntaTM)
	descripcion = models.CharField(max_length=100)
	correcta = models.BooleanField(default=False)

class PreguntaMoss(models.Model):
	descripcion = models.CharField(max_length=150)

class RespuestaMoss(models.Model):
	pregunta = models.ForeignKey(PreguntaMoss)
	descripcion = models.CharField(max_length=100)
	correcta = models.BooleanField(default=False)


class PreguntaGordon(models.Model)
	respuesta_1 = models.CharField(max_length=150)
	respuesta_2 = models.CharField(max_length=150)
	respuesta_3 = models.CharField(max_length=150)
	respuesta_4 = models.CharField(max_length=150)


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