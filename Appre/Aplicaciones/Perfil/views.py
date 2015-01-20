from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Perfil(TemplateView):
	template_name= 'perfil/Perfil.html'
