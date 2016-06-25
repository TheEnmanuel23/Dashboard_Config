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

    def get_success_url(self):
        return reverse_lazy( 'get_update_layers', kwargs = {
            'pk' : self.kwargs['pk']
        })

class AddLayer( UpdateView ):
    model = Image
    template_name = "layers/create_layer.html"
    fields = [
        'descripcion',
        'imagen',
    ]

    def get_context_data( self, **kwargs ):
        context = super( AddLayer, self ).get_context_data( **kwargs )
        project = Proyecto.objects.get( pk=self.object.proyecto.pk )
        context[ 'project' ] = project
        context[ 'LayerFormSet' ] = LayerFormSet()
        context[ 'singleImage' ] = self.object
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

    def get_success_url(self):
        return reverse_lazy( 'add_layer', kwargs = {
            'idproject':self.kwargs['idproject'],
            'pk' : self.kwargs['pk']
        })


class ListLayersJson( ListView ):
    model = Capa

    def get( self, request, *args, **kwargs ):
        idImage = request.GET.get('image', None)
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

class ListLayersView( ListView):
    model = Capa
    template_name = 'layers/listLayers.html'
    context_object_name = 'listLayers'

    def get_queryset(self):
        idImage = self.kwargs['image']
        queryset = Capa.objects.filter(image__pk = idImage)
        return queryset;

    def get_context_data( self, **kwargs ):
        idImage = self.kwargs['image']
        context = super( ListLayersView, self ).get_context_data( **kwargs )
        image = Image.objects.get(pk = idImage)
        project = Proyecto.objects.get( pk= image.proyecto.pk )
        context[ 'singleImage' ] = image
        context[ 'project' ] = project
        return context

class DeleteLayer(DeleteView):
    model = Capa
    template_name = 'layers/deleteLayer.html'
    context_object_name = 'deleteLayer'

    def get_context_data(self, **kwargs):
        context= super(DeleteLayer, self).get_context_data(**kwargs)
        image = Image.objects.get(pk = self.object.image.pk)
        project = Proyecto.objects.get(pk = image.proyecto.pk)
        context[ 'singleImage' ] = image
        context[ 'project' ] = project
        return context

    def get_success_url(self):
        image = Image.objects.get(pk = self.object.image.pk)
        return reverse_lazy('get_layer_view', kwargs={'image': image.pk})


class IndicadorList(ListView):
    model = Indicador
    template_name = "indicadores/list_indicadores.html"
    context_object_name = 'listIndicadores'

    def get_queryset(self):
        idProject = self.kwargs['pk']
        queryset = Indicador.objects.filter(proyecto__pk = idProject)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndicadorList, self).get_context_data(**kwargs)
        idProject = self.kwargs['pk']
        image = Image.objects.get(proyecto__pk = idProject)
        project =image.proyecto
        context[ 'singleImage' ] = image
        context[ 'project' ] = project
        return context

class UpdateIndicador(UpdateView):
    model = Indicador
    template_name = 'indicadores/update_indicador.html'
    fields = [
        'descripcion',
        'proyecto'
    ]

    def get_context_data(self, **kwargs):
        context = super(UpdateIndicador, self).get_context_data(**kwargs)
        image = Image.objects.get(proyecto__pk = self.object.proyecto.pk)
        project = self.object.proyecto
        context[ 'singleImage' ] = image
        context[ 'project' ] = project
        return context

    def get_success_url(self):
        return reverse_lazy('indicadorList', kwargs = { 'pk' : self.object.proyecto.pk })

class DeleteIndicador(DeleteView):
    model = Indicador
    template_name = 'indicadores/delete_indicador.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteIndicador, self).get_context_data(**kwargs)
        image = Image.objects.get(proyecto__pk = self.object.proyecto.pk)
        project = self.object.proyecto
        context[ 'singleImage' ] = image
        context[ 'project' ] = project
        return context

    def get_success_url(self):
        return reverse_lazy('indicadorList', kwargs = { 'pk' : self.object.proyecto.pk })

class CreateIndicador(CreateView):
    model = Proyecto
    template_name = 'indicadores/create_indicador.html'
    fields = [ 'nombre', 'descripcion' ]

    def get_context_data(self, **kwargs):
        context = super(CreateIndicador, self).get_context_data(**kwargs)
        idProject = self.kwargs['pk']
        image = Image.objects.get(proyecto__pk = idProject)
        project = image.proyecto
        context[ 'IndicadorFormSet' ] = IndicadorFormSet()
        context[ 'singleImage' ] = image
        context[ 'project' ] = project
        return context

    def post( self, request, *args, **kwargs ):
        idProject = self.kwargs['pk']
        self.object = Proyecto.objects.get(pk = idProject)
        indicadorFormSet = IndicadorFormSet( request.POST, instance=self.object )
        if (indicadorFormSet.is_valid( )):
            return self.form_valid( indicadorFormSet )

    def form_valid( self, indicadorFormSet ):
        indicadorFormSet.save( )
        return HttpResponseRedirect( self.get_success_url( ) )

    def get_success_url(self):
        return reverse_lazy('indicadorList', kwargs = { 'pk' : self.kwargs['pk'] })