from django.db import models

# Create your models here.
class Camarero(models.Model):
	nombre = models.CharField(max_length=100)
	dni = models.CharField(max_length=9)

class Factura(models.Model):
	camarero = models.ForeignKey(Camarero)
	fecha = models.DateTimeField()
	
class Articulo(models.Model):
	articulo = models.CharField(max_length=100)
	precio_unitario = models.FloatField()
	
class Cantidad(models.Model):
	cantidad = models.IntegerField()
	articulo = models.ForeignKey(Articulo)
	factura = models.ForeignKey(Factura)

class Periodo(models.Model):
	fecha_inicio = models.DateTimeField()
	fecha_fin = models.DateTimeField()
	camarero = models.ForeignKey(Camarero)
	class Meta:
		unique_together = (('fecha_inicio', 'camarero'),)

class Saldo(models.Model):
	fecha_saldo = models.DateTimeField()
	saldo_actual = models.FloatField()
	
	