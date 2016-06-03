from django.shortcuts import render
from appTpv.models import Articulo, Camarero, Factura, Cantidad #del models importa la clase Articulo Factura, Cantidad
from django.core import serializers
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404


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

def meterMasArticulos(request,factura_id,articulo_id):
	factura_actual = get_object_or_404(Factura, pk=factura_id)
	articulo_actual = get_object_or_404(Articulo, pk=articulo_id)
	cantidad = Cantidad.objects.filter(factura=factura_actual,articulo=articulo_actual)
	if cantidad:
		c=cantidad[0]
		c.cantidad=c.cantidad+1
		c.save()
	else:
		c = Cantidad(articulo=articulo_actual,factura=factura_actual,cantidad=1)
		c.save()
	resultado = {'result':'OK'}
	return HttpResponse(json.dumps(resultado, cls=DjangoJSONEncoder), content_type='application/json')

def ticketNuevo(request,camarero_id): #request es la peticion que nos llega en http, el id es el parametro que va en esa peticion
	#print("ticket nuevo de "+camarero)	
	#tickets = Factura.objects.all()
	#camarero_actual = Camarero.objects.get(nombre=camarero) #esto es una variable que guarda el nombre del Camarero, esta relacionada con 		#Factura porque factura es clave ajena de Camarero
	
	
	#data = serializers.serialize('json', [camarero_actual,])
	#struct = json.loads(data)
	#data = json.dumps(struct[0])
	#return HttpResponse(data, mimetype='application/json')
	camarero_actual = get_object_or_404(Camarero, pk=camarero_id) #	con el id del camarero sacamos el objeto de camarero con todos sus campos
	f = Factura(camarero = camarero_actual, abierto = True) #creamos una factura nueva que asignamos a ese camarero
	f.save() # guardamos la factura
	resultado = {'fecha':f.fecha,'id':f.id} # devolvemos el id y la fecha de la factura ya que lo necesitas el id y la fecha de la factura (al crear una factura nueva le pasas la fecha y el id pa crear esta
	return HttpResponse(json.dumps(resultado, cls=DjangoJSONEncoder), content_type='application/json') #esto devuelve un Json con 'result':'OK'
#devuelve la variable resultado serializada osea pasada de json a bits content type es un protocolo http nos indica el formato que es

