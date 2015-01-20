from django.contrib import admin

from .models import Empresa ,Proyecto

class AdminEmpresa(admin.ModelAdmin):
	list_display = ('nombre_empresa','giro')

admin.site.register(Empresa,AdminEmpresa)

class AdminProyecto(admin.ModelAdmin):
	list_display = ('nombre_proyecto','opcion_elegida')

admin.site.register(Proyecto,AdminProyecto)
