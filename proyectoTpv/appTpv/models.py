from django.db import models
import datetime

# Create your models here.
class Camarero(models.Model):
	nombre = models.CharField(max_length=50)
	dni = models.CharField(max_length=9)
	def __str__(self):
		return '%s' % (self.id)

class Factura(models.Model):
	camarero = models.ForeignKey(Camarero)
	fecha = models.DateTimeField(default=datetime.datetime.now)
	abierto = models.NullBooleanField()
	def __str__(self):
		return '%s' % (self.id)
	
	
class Articulo(models.Model):
	nombre = models.CharField(max_length=50)
	precio_unitario = models.FloatField()
	def __str__(self):
		return '%s' % (self.nombre)
	
class Cantidad(models.Model):
	cantidad = models.IntegerField()
	articulo = models.ForeignKey(Articulo)
	factura = models.ForeignKey(Factura)
	def __str__(self):
		return '%s' % (self.articulo)

class Periodo(models.Model):
	fecha_inicio = models.DateTimeField()
	fecha_fin = models.DateTimeField(null=True,blank=True)
	camarero = models.ForeignKey(Camarero)
	class Meta:
		unique_together = (('fecha_inicio', 'camarero'),)
	def __str__(self):
		return '%s' % (self.camarero)

class Saldo(models.Model):
	fecha_saldo = models.DateTimeField()
	saldo_actual = models.FloatField()
	def __str__(self):
		return '%s' % (self.saldo_actual)
	
	
