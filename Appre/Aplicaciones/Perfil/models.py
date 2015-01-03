from django.db import models
# Importo libreria del tiempo
from django.utils import timezone
# Importo el usuario
from django.contrib.auth.models import User
# Importo el timedelta  para aumentar dias a los modelos
from datetime import datetime, timedelta



# MODELO PERFILES
class Perfil(models.Model):
	Email=models.EmailField(max_length=75)
	Nombre=models.CharField(max_length=100)
	Apellido_p=models.CharField(max_length=100)
	Apellido_m=models.CharField(max_length=100)
	Avatar=models.ImageField()
	Ncontrol=models.CharField(max_length=100)
	TelefonoMovil=models.IntegerField()
		
	def __unicode__(self):
		return self.nombre
