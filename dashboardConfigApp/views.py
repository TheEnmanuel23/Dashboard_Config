from django.shortcuts import render, redirect, get_object_or_404
from dashboardConfigApp.forms import *
from django.http import HttpResponseRedirect
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def proyecto_nuevo(request):
	if(request.method == 'POST'):
		formProyecto = ProyectForm(request.POST)
		formImage = ImageForm(request.POST, request.FILES)

		if formProyecto.is_valid() and formImage.is_valid():
			proyecto = formProyecto.save()
			image = formImage.save(commit = False)
			image.proyecto = proyecto
			image.save()
			return HttpResponseRedirect("/")

	formProyecto = ProyectForm()
	formImage = ImageForm()
	data = {
		'formProyecto': formProyecto, 'formImage': formImage
	}
	return render(request, 'new_project.html', data)

def GetLayersByProject(request, idProject):
	if(request.method == 'GET'):
		imagesList = Image.objects.filter(proyecto__pk = idProject)
		singleImage = Image.objects.get(proyecto__pk = idProject)
		layers =  Capa.objects.filter(image__in = imagesList)
		dictionary = {
			'layers': layers,
			'singleImage': singleImage
		}
		return render(request, "projectInfo.html", dictionary)

@api_view(['GET','POST', 'PUT'])
def GetAllProjectApi(request):
	if(request.method == 'GET'):
		queryset = Proyecto.objects.all().order_by('-fechaCreacion')
		serializer = ProjectSerializer(queryset, many =True)
		return Response(serializer.data)


def GetAllProject(request):
	if(request.method == 'GET'):
		queryset = Proyecto.objects.all().order_by('-fechaCreacion')
		#projects = ProjectSerializer(queryset, many =True)
		dictionary = {
			'projects': queryset
		}
		return render(request, "index.html", dictionary)

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