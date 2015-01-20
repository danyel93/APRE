from django.conf.urls import patterns, include, url
from .views import Perfil

urlpatterns = patterns('',
	url(r'^Perfil/$' , Perfil.as_view() ),
	
                              
)