from django.shortcuts import render, redirect
from dashboardConfigApp.forms import *

# Create your views here.
def home_view(request):
    return render('index.html')

def proyecto_nuevo(request):	
	formProyecto = ProyectForm()
	formImage = ImageForm();
	if(request.method == 'POST'):
		formProyecto = ProyectForm(request.POST, request.FILES)
		return redirect('/')

	return render(request, 'new_project.html', {'formProyecto': formProyecto, 'formImage' : formImage})
