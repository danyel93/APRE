from django.db import models
# Importo libreria del tiempo
from django.utils import timezone
from datetime import datetime, timedelta
# Importo el modelo de la aplicacion Perfil
from Aplicaciones.Perfil.models import Perfil, Carrera
# Importo Modelos de la aplicacion Docentes
from Aplicaciones.Docentes.models import Asesor_Interno

#Modelo Empresa
class Empresa(models.Model):
	# Campos Normales
	nombre_empresa = models.CharField(max_length=250,null=True,blank=True)
	giro = models.CharField(max_length=250,null=True,blank=True)

	def __unicode__(self):
		return self.nombre_empresa

# Modelo Proyecto
class Proyecto(models.Model):
	# LLave Foraneas
	carrera = models.ForeignKey(Carrera,null=True,blank=True)
	asesor_interno = models.ForeignKey(Asesor_Interno,null=True,blank=True)
	empresa = models.OneToOneField(Empresa,null=True,blank=True)
	# Campos Normales
	nombre_proyecto = models.CharField(max_length=250,null=True,blank=True)
	opcion_elegida = models.CharField(max_length=50,null=True,blank=True)

	def __unicode__(self):
		return self.nombre_poryecto
