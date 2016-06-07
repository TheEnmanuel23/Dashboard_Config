from django.db import models
from django.utils import timezone

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.nombre

class Image(models.Model):
	descripcion = models.CharField(max_length=100)
	imagen = models.FileField(upload_to='images/', default='images/none_image.jpg')
	proyecto = models.ForeignKey(Proyecto)

	def __str__(self):
		return self.imagen.name

class Capa(models.Model):
	descripcion = models.CharField(max_length=140)
	image = models.ForeignKey(Image)

class TipoCampo(models.Model):
	descripcion = models.CharField(max_length=10)

class Indicador(models.Model):
	descripcion = models.CharField(max_length=200)
	tipo = models.ForeignKey(TipoCampo)

class Condicion(models.Model):
	descripcion = models.CharField(max_length=100)
	tipo = models.CharField(max_length=5)

class Capa_Indicador(models.Model):
	indicador = models.ForeignKey(Indicador)
	capa = models.ForeignKey(Capa)
	valor = models.CharField(max_length=100)

class Condicion_Indicador(models.Model):
	indicador = models.ForeignKey(Indicador)	
	codicion = models.ForeignKey(Condicion)
	valorComparar = models.CharField(max_length=20)
	color = models.CharField(max_length=11)

class Condicion_Capa(models.Model):
	capa = models.ForeignKey(Capa)	
	codicion = models.ForeignKey(Condicion)
	color = models.CharField(max_length=11)