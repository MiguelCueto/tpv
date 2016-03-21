from django.shortcuts import render
from appTpv.models import Articulo, Camarero, Factura, Cantidad #del models importa la clase Articulo
from django.core import serializers
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

def indice(request):
	lista_Articulo = Articulo.objects.all()#en esta variable metes todos los art
	lista_Camarero = Camarero.objects.all()
	return render(request, 'appTpv/indice.html',{'lista_Articulo':lista_Articulo,'lista_Camarero':lista_Camarero})
#esta funcion devuelve una peticion a la plantilla que esta en la carpeta
#appTpv/indice.html
#{'lista_Articulo':lista_Articulo} nos dice como se va a llamar la variable que #contiene todos los datos del modelo en el html
#osea como se va a llamar lista_Articulo en el template

def tickets_abiertos(request,camarero):
	lista_tickets = Cantidad.objects.filter(factura__abierto=True,factura__camarero__nombre=camarero).values('factura__camarero__nombre','factura','articulo__nombre','articulo__precio_unitario','cantidad','factura__fecha')
	print(lista_tickets)
	return HttpResponse(json.dumps(list(lista_tickets), cls=DjangoJSONEncoder), content_type='application/json')


