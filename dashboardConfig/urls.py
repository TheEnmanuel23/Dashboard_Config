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
    url(r'^$', home_view, name="home"),
    url(r'^new_project/', proyecto_nuevo, name="new_project"),
    url(r'^get_layers/project/(\d+)$', LayersApi, name='get-layers'),    
    url(r'^get_all_projects/', GetAllProjectApi, name='get_all_projects'),
    url(r'^get_all_images/', GetAllImageApi, name='get_all_images'),
    url(r'^filter_images_by_project/(\d+)$', GetAllImageApiByProject, name='filter_images_by_project'),
    
]
