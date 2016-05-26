from django.conf.urls import include, url
from appTpv import views

urlpatterns = [
   
    url(r'^$',views.indice,name='indice'),
#  cadena vacia. llama a la vista indice, con el nombre de enlace: indice
	url(r'^tickets_abiertos/(?P<camarero>\w+)/$',views.tickets_abiertos, name='tickets_abiertos'),
	url(r'^meterMasArticulos/(?P<factura_id>\d+)/(?P<articulo_id>\d+)/$',views.meterMasArticulos,name='meterMasArticulos'),
#A continuación vamos a crear la url que nos cree tickets nuevos 
	url(r'^ticketNuevo/(?P<camarero>\w+)/$',views.ticketNuevo, name='ticketNuevo'),
]
