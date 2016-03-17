from django.shortcuts import render
from appTpv.models import Articulo, Camarero #del models importa la clase Articulo

# Create your views here.

def indice(request):
	lista_Articulo = Articulo.objects.all()#en esta variable metes todos los art
	lista_Camarero = Camarero.objects.all()
	return render(request, 'appTpv/indice.html',{'lista_Articulo':lista_Articulo,'lista_Camarero':lista_Camarero})
#esta funcion devuelve una peticion a la plantilla que esta en la carpeta
#appTpv/indice.html
#{'lista_Articulo':lista_Articulo} nos dice como se va a llamar la variable que #contiene todos los datos del modelo en el html
#osea como se va a llamar lista_Articulo en el template


