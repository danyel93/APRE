from django.db import models
# Importo libreria del tiempo
from django.utils import timezone
# Importo el usuario
from django.contrib.auth.models import User
# Importo el timedelta  para aumentar dias a los modelos
from datetime import datetime, timedelta

# MODELO LLAVES PARA JEFES DE CARRERA Y ASESORES INTERNOS
class Codigo(models.Model):
	# Campos Normales
	tipo = models.CharField(max_length=50)
	llave = models.CharField(max_length=100)
	fecha_creada = models.DateField(default=timezone.now)
	fecha_caducidad = models.DateField(default=timezone.now()+timedelta(days=7))
	validada = models.BooleanField(default=False)
	def __unicode__(self):
		return self.llave

# MODELO PARA LAS CARRERAS QUEDARAN VINCULADAS DESDE EL PERFIL
class Carrera(models.Model):
	plan_estudios = models.CharField(max_length=100,null=True,blank=True)
	nombre_carrera = models.CharField(max_length=100, null=True , blank=True)
	modalidad = models.CharField(max_length=100,null=True ,blank=True)
	def __unicode__(self):
		return self.nombre_carrera 

# MODELO PERFILES
class Perfil(models.Model):
	# Relaciones BD
	usuario = models.OneToOneField(User, null=True, blank=True)
	codigo = models.OneToOneField(Codigo,null=True,blank=True)
	# Campos Normales
	nombre = models.CharField(max_length=50)
	apellido_p = models.CharField(max_length=50)
	apellido_m = models.CharField(max_length=50)
	numero_control = models.CharField(max_length=150)
	tel_movil = models.CharField(max_length=50)
	avatar = models.ImageField(upload_to='Imagenes/avatares/%Y/%m/%d')
	fecha_registro = models.DateField(default=timezone.now)
	tipo_usuario = models.CharField(max_length=50,null=True,blank=True)
	editar = models.BooleanField(default=True)
	activo = models.BooleanField(default=False)
	
		
	def __unicode__(self):
		return self.usuario


