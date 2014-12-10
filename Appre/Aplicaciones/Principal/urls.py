from django.conf.urls import patterns, include, url
from .views import Principal

urlpatterns = patterns('',
   # url de la la Pagina principal
    url(r'^$',Principal.as_view()),  
                         
)