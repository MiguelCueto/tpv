from django.conf.urls import include, url
from appTpv import views

urlpatterns = [
   
    url(r'^$',views.indice,name='indice'),
#  cadena vacia. llama a la vista indice, con el nombre de enlace: indice
	url(r'^tickets_abiertos/(?P<camarero>\w+)/$',views.tickets_abiertos, name='tickets_abiertos'),
]
