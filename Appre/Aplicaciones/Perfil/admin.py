from django.contrib import admin
from .models import Perfil, Codigo , Carrera

class AdminCarrera(admin.ModelAdmin):
	list_display = ('plan_estudios','nombre_carrera')

admin.site.register(Carrera,AdminCarrera)

class AdminPerfil(admin.ModelAdmin):
	list_display = ('usuario','nombre')

admin.site.register(Perfil,AdminPerfil)

class AdminCodigo(admin.ModelAdmin):
	list_display = ('fecha_creada','tipo')

admin.site.register(Codigo,AdminCodigo)