from django.db import models
# Importo libreria del tiempo
from django.utils import timezone
# Importo el usuario
from django.contrib.auth.models import User
# Importo el timedelta  para aumentar dias a los modelos
from datetime import datetime, timedelta
# Importo Modelos de otra aplicacion Perfil
from Aplicaciones.Perfil.models import Perfil, Carrera
# Importo Modelos de la aplicacion Docentes
from Aplicaciones.Docentes.models import Asesor_Interno
# Importo Aplicacion Residencias 
from Aplicaciones.Residencia.models import Proyecto

# Modelo Cronograma
class Cronograma(models.Model):
	objetivos_especificos = models.TextField()
	etapa_1 = models.CharField(max_length=100,null=True,blank=True)
	etapa_2 = models.CharField(max_length=100,null=True,blank=True)
	etapa_3 = models.CharField(max_length=100,null=True,blank=True)
	c1_ai = models.BooleanField(default=False)
	c2_ai = models.BooleanField(default=False)
	c3_ai = models.BooleanField(default=False)
	def __unicode__(self):
		return self.usuario

# Modelo Alumno
class Alumno(models.Model):
	# Relaciones BD
	proyecto = models.ForeignKey(Proyecto,null=True,blank=True)
	cronograma = models.OneToOneField(Cronograma, null=True, blank=True)
	perfil = models.OneToOneField(Perfil,null=True,blank=True)
	carrera = models.ForeignKey(Carrera,null=True,blank=True)
	asesor_interno = models.ForeignKey(Asesor_Interno,null=True,blank=True)
	# Campos Normales
	calle = models.CharField(max_length=250,null=True,blank=True)
	numero_casa = models.CharField(max_length=10,null=True,blank=True)
	colonia = models.CharField(max_length=100,null=True,blank=True)
	tipo_seguro = models.CharField(max_length=50,null=True,blank=True)
	num_seguro = models.CharField(max_length=20,null=True,blank=True)
	ciudad = models.CharField(max_length=100,null=True,blank=True)
	tel_casa = models.CharField(max_length=20,null=True,blank=True)
	cali_ai = models.PositiveSmallIntegerField(max_length=3,null=True,blank=True)
	cali_ae = models.PositiveSmallIntegerField(max_length=3,null=True,blank=True)
	cali_final = models.PositiveSmallIntegerField(max_length=3,null=True,blank=True)
	intentos = models.TextField()


	def __unicode__(self):
		return self.usuario