from django import forms
from dashboardConfigApp.models import *

class ProyectForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = [
			'nombre',
		]

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = [
			'descripcion',
			'imagen',
		]

class CapaIndicadorForm(forms.ModelForm):
	class Meta:
		model = Condicion_Indicador
		fields = [
			'valorComparar',
			'color',
		]