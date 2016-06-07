from django.shortcuts import render, redirect
from dashboardConfigApp.forms import *
from django.http import HttpResponseRedirect
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
			HttpResponseRedirect("/")

	formProyecto = ProyectForm()
	formImage = ImageForm()
	data = {
		'formProyecto': formProyecto, 'formImage': formImage
	}
	return render(request, 'new_project.html', data)
