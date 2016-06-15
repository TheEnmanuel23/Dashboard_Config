from django import forms
from dashboardConfigApp.models import *

class ProyectForm(forms.ModelForm):
	descripcion = forms.CharField(widget=forms.Textarea())
	class Meta:
		model = Proyecto
		fields = [
			'nombre',
			'descripcion'
		]

class ImageForm(forms.ModelForm):	
	descripcion = forms.CharField(widget=forms.Textarea())
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