"""dashboardConfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dashboardConfigApp.views import *
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^$', GetAllProject.as_view(), name="home"),
    url(r'^new_project/', CreateNewProject.as_view(), name="new_project"),
    url(r'^project/(\d+)$', GetInfoProject, name='configProject'),
    url(r'^editProject/(?P<pk>\d+)$', EditProject.as_view(), name='editProject'),
    url(r'^deleteProject/(?P<pk>\d+)$', DeleteProject.as_view(), name='deleteProject'),
    url(r'^project/image/(?P<pk>\d+)/get_layers/', GetAndUpdateLayers.as_view(), name='get_update_layers'),
    url(r'^project/(?P<idproject>\d+)/image/(?P<pk>\d+)/add_layers/', AddLayer.as_view(), name='add_layer'),
    url(r'^project/layers/', ListLayersJson.as_view(), name='get_layer_json'),
    url(r'^project/image/(?P<image>\d+)/delete_layers/', ListLayersView.as_view(), name='get_layer_view'),
    url(r'^deleteLayer/(?P<pk>\d+)$', DeleteLayer.as_view(), name='deleteLayer'),
    url(r'^project/(?P<pk>\d+)/indicador', IndicadorList.as_view(), name='indicadorList'),
    url(r'^project/(\d+)/updateIndicador/(?P<pk>\d+)', UpdateIndicador.as_view(), name='updateIndicador'),
    url(r'^project/(\d+)/deleteIndicador/(?P<pk>\d+)', DeleteIndicador.as_view(), name='deleteIndicador'),
    url(r'^project/(?P<pk>\d+)/add_indicador/', CreateIndicador.as_view(), name='add_indicador'),


]
