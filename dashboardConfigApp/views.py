from django.shortcuts import render, redirect
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

@api_view(['GET','POST', 'PUT'])
def LayersApi(request, idImage):
	if(request.method == 'GET'):
		queryset = Capa.objects.all()
		serializer = CapaSerializer(queryset, many =True)
		return Response(serializer.data)

@api_view(['GET','POST', 'PUT'])
def GetAllProjectApi(request):
	if(request.method == 'GET'):
		queryset = Proyecto.objects.all()
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