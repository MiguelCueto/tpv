from django.conf.urls import include, url
from appTpv import views

urlpatterns = [
   
    url(r'^$',views.indice,name='indice')
#  cadena vacia. llama a la vista indice, con el nombre de enlace: indice
]
