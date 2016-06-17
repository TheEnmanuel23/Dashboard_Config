from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from dashboardConfigApp.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.views import generic
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class GetAllProject(generic.ListView):
	template_name = 'index.html'
	context_object_name ='listAllProject'
	model = Proyecto
	def get_queryset(self):
		return Proyecto.objects.all().order_by('-fechaCreacion')

class EditProject(UpdateView):
	model = Proyecto
	template_name = 'editProject.html'
	context_object_name = 'editProject'
	success_url = reverse_lazy('home')
	fields = [
		'nombre',
		'descripcion'
	]
class DeleteProject(DeleteView):
	model = Proyecto
	template_name = 'deleteProject.html'
	context_object_name = 'deleteProject'
	success_url = reverse_lazy('home')

class CreateNewProject(CreateView):
	form_class = NewProjectForm
	success_url = reverse_lazy('home')
	template_name ='new_project.html'

def GetInfoProject(request, idProject):
	if(request.method == 'GET'):
		project = Proyecto.objects.get(pk = idProject)
		singleImage = Image.objects.get(proyecto__pk = idProject)
		dictionary = {
			'project': project,
			'singleImage': singleImage
		}
		return render(request, "projectInfo.html", dictionary)

def ConfigLayers(request, idProject=None):
	if idProject:
		imagesList = Image.objects.filter(proyecto__pk = idProject)
		layers =  Capa.objects.filter(image__in = imagesList).values()
		singleImage = Image.objects.get(proyecto__pk = idProject)
	else:
		layers = Capa()
		singleImage = Image()

	LayerFormSet = inlineformset_factory(Image, Capa,fields=('idCapa', 'descripcion'), extra = 0)

	if(request.method == 'GET'):
		project = Proyecto.objects.get(pk = idProject)
		layerFormset = LayerFormSet(instance=singleImage)
	elif(request.method == 'POST'):
		layerFormset = LayerFormSet(request.POST, instance=singleImage)
		if(layerFormset.is_valid()):
			layerFormset.save()
			return HttpResponseRedirect("home")
	dictionary = {
			'project': project,
			'layers': layers,
			'singleImage': singleImage,
			'layerFormset': layerFormset
		}
	return render(request, "layers.html", dictionary)

@api_view(['GET','POST', 'PUT'])
def GetAllProjectApi(request):
	if(request.method == 'GET'):
		queryset = Proyecto.objects.all().order_by('-fechaCreacion')
		serializer = ProjectSerializer(queryset, many =True)
		return Response(serializer.data)

@api_view(['GET','POST', 'PUT'])
def GetAllImageApi(request):
	if(request.method == 'GET'):
		queryset = Image.objects.all()
		serializer = ImageSerializer(queryset, many =True)
		return Response(serializer.data)

@api_view(['GET','POST', 'PUT'])
def GetAllImageApiByProject(request, idProject):
	if(request.method == 'GET'):
		queryset = Image.objects.all()
		serializer = ImageSerializer(queryset, many =True)
		return Response(serializer.data)