from django.db import models
# Importo libreria del tiempo
from django.utils import timezone
# Importo el usuario
from django.contrib.auth.models import User
# Importo el timedelta  para aumentar dias a los modelos
from datetime import datetime, timedelta
# Importo del Modelo Perfil
from Aplicaciones.Perfil.models import Perfil, Carrera

class Asesor_Interno(models.Model):
	# Llave Foraneas
	perfil = models.ForeignKey(Perfil,null=True,blank=True)
	# Campos Normales
	departamento = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.perfil