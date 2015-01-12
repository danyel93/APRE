from django.contrib import admin

from .models import Asesor_Interno

class AdminAsesor_Interno(admin.ModelAdmin):
	list_display = ('perfil','departamento')

admin.site.register(Asesor_Interno,AdminAsesor_Interno)

