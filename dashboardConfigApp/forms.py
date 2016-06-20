from django import forms
from dashboardConfigApp.models import *
from django.forms.models import inlineformset_factory
from betterforms.multiform import MultiModelForm

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

class NewProjectForm(MultiModelForm):
	form_classes = {
		'project': ProjectForm,
		'image': ImageForm
	}

	def save(self, commit=True):
		objects =  super(NewProjectForm, self).save(commit=False)
		if(commit):
			project = objects['project']
			project.save()
			image = objects['image']
			image.proyecto = project
			image.save()
			return objects

class LayerForm(forms.ModelForm):
	class Meta:
		model = Capa
		fields = [
			'descripcion',
			'idCapa',
		]


LayerFormSet = inlineformset_factory(Image, Capa, extra=0, form = LayerForm)
class CapaIndicadorForm(forms.ModelForm):
	class Meta:
		model = Condicion_Indicador
		fields = [
			'valorComparar',
			'color',
		]