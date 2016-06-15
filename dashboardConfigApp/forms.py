from django import forms
from dashboardConfigApp.models import *

class ProjectForm(forms.ModelForm):
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

class LayerForm(forms.ModelForm):
	class Meta:
		model = Capa
		fields = [
			'descripcion',
			'idCapa',
		]
class CapaIndicadorForm(forms.ModelForm):
	class Meta:
		model = Condicion_Indicador
		fields = [
			'valorComparar',
			'color',
		]