from django.shortcuts import render
# Importando las clases del TemplateView
from django.views.generic import TemplateView

class Principal(TemplateView):
	template_name = 'Principal/Principal.html'
