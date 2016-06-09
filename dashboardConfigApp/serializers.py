from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proyecto
		fields = ('nombre', 'fechaCreacion',)

class TipoCampoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoCampo

class ImageSerializer(serializers.ModelSerializer):
	proyecto = ProjectSerializer
	class Meta:
		model = Image
		fields = ('imagen', 'descripcion', 'proyecto')

class CapaSerializer(serializers.ModelSerializer):
	image = ImageSerializer
	class Meta:
		model = Indicador
		fields = ('codigo', 'descripcion', 'image')