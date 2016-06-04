from django.db import models

# Create your models here.
class Condicion(models.Model):
	descripcion = models.CharField(max_length=100)
	tipo = models.CharField(max_length=5)

class Proyect(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    nombre = models.CharField(max_length=100)

class Image(models.Model):
	proyecto = models.ForeignKey(Proyect)
	descripcion = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/', default='images/none_image.jpg')

class DataImage(models.Model):
	image = models.ForeignKey(Image)
	descripcion = models.CharField(max_length=140)
	condicion = models.ForeignKey(Condicion)
	color = models.CharField(max_length=11)

class CustomTypeField(models.Model):
	descripcion = models.CharField(max_length=10)

class Indicador(models.Model):
	descripcion = models.CharField(max_length=200)
	tipo = models.ForeignKey(CustomTypeField)
	color = models.CharField(max_length=11)
	compareToValue = models.CharField(max_length=20)

class DataImage_Indicador(models.Model):
	indicador = models.ForeignKey(Indicador)
	dataImage = models.ForeignKey(DataImage)
	valor = models.CharField(max_length=100)