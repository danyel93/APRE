from django.contrib import admin

from .models import Alumno , Cronograma

class AdminAlumno(admin.ModelAdmin):
	list_display = ('perfil','cronograma')

admin.site.register(Alumno,AdminAlumno)

class AdminCronograma(admin.ModelAdmin):
	list_display = ('etapa_1','etapa_2')

admin.site.register(Cronograma,AdminCronograma)