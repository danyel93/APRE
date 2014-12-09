from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Appre.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
    
    # url de la aplicacion C_inicio
    url(r'^',include('Aplicaciones.Perfil.urls')),

    # Url para vizualizar las todas las posibles imagenes 
    url(r'Imagenes/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT, } ),
)

