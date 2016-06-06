from django.contrib import admin

# Register your models here.
from dashboardConfigApp.models import *

admin.site.register(Proyecto)
admin.site.register(Image)
admin.site.register(Capa)
admin.site.register(TipoCampo)
admin.site.register(Indicador)
admin.site.register(Condicion)
admin.site.register(Capa_Indicador)
admin.site.register(Condicion_Indicador)
admin.site.register(Condicion_Capa)
