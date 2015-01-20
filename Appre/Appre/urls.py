from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Appre.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url del administrador de django  
	url(r'^admin/', include(admin.site.urls)),
    # url de la Aplicacion Principal(pagina de Inicio)
    url(r'^',include('Aplicaciones.Principal.urls')),
    # url de la aplicacion Perfil
    url(r'^Perfil/',include('Aplicaciones.Perfil.urls')),
    # url de la aplicacion Docentes
    url(r'^Perfil/',include('Aplicaciones.Docentes.urls')),
    # url de la seccion de registro, perfil y logeo
    url(r'^accounts/', include('allauth.urls')),
    # Url para vizualizar las todas las posibles imagenes 
    url(r'Imagenes/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT, } ),
    # Url para visualizar los datos del perfil
    url(r'^' , include('Aplicaciones.Perfil.urls')),   
)

