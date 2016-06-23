from django.shortcuts import render
from dashboardConfigApp.forms import *
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView
from .serializers import *
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy


# Create your views here.

class GetAllProject( generic.ListView ):
    template_name = 'index.html'
    context_object_name = 'listAllProject'
    model = Proyecto
    paginate_by = 2

    def get_queryset( self ):
        return self.model.objects.all( ).order_by( '-fechaCreacion' )


class EditProject( UpdateView ):
    model = Proyecto
    template_name = 'project/editProject.html'
    context_object_name = 'editProject'
    success_url = reverse_lazy( 'home' )
    fields = [
        'nombre',
        'descripcion',
    ]


class DeleteProject( DeleteView ):
    model = Proyecto
    template_name = 'project/deleteProject.html'
    context_object_name = 'deleteProject'
    success_url = reverse_lazy( 'home' )


class CreateNewProject( CreateView ):
    form_class = NewProjectForm
    success_url = reverse_lazy( 'home' )
    template_name = 'project/new_project.html'


def GetInfoProject( request, idProject ):
    if (request.method == 'GET'):
        project = Proyecto.objects.get( pk=idProject )
        singleImage = Image.objects.get( proyecto__pk=idProject )
        dictionary = {
            'project': project,
            'singleImage': singleImage
        }
        return render( request, "project/projectInfo.html", dictionary )


class GetAndUpdateLayers( UpdateView ):
    model = Image
    template_name = 'layers/getAndEditLayers.html'
    success_url = reverse_lazy( 'home' )
    fields = [
        'imagen',
        'descripcion'
    ]

    def get_context_data( self, **kwargs ):
        context = super( GetAndUpdateLayers, self ).get_context_data( **kwargs )
        project = Proyecto.objects.get( pk=self.object.proyecto.pk )
        context[ 'LayerFormSet' ] = LayerFormSet( instance=self.object )
        context[ 'singleImage' ] = self.object
        context[ 'project' ] = project
        return context

    def post( self, request, *args, **kwargs ):
        self.object = self.get_object( )
        layerFormSet = LayerFormSet( request.POST, instance=self.object )
        if (layerFormSet.is_valid( )):
            return self.form_valid( layerFormSet )

    def form_valid( self, layerFormSet ):
        layerFormSet.instance = self.object
        layerFormSet.save( )
        return HttpResponseRedirect( self.get_success_url( ) )


class AddLayer( UpdateView ):
    model = Image
    template_name = "layers/create_layer.html"
    success_url = reverse_lazy( 'home' )
    fields = [
        'descripcion',
        'imagen',
    ]

    def get_context_data( self, **kwargs ):
        context = super( AddLayer, self ).get_context_data( **kwargs )
        project = Proyecto.objects.get( pk=self.object.proyecto.pk )
        context[ 'project' ] = project
        context[ 'LayerFormSet' ] = LayerFormSet( )
        context[ 'singleImage' ] = self.object
        return context


class ListLayers( ListView ):
    model = Capa

    def get( self, request, *args, **kwargs ):
        idImage = request.GET.get('image')
        self.object_list = self.model.objects.filter(image__pk = idImage)
        return self.json_to_response( )

    def json_to_response( self ):
        data = list( )
        for layer in self.object_list:
            data.append( {
                'idCapa': layer.idCapa,
                'descripcion': layer.descripcion,
                'image': layer.image.imagen.url
            } )
        return JsonResponse( data, safe=False )