from django.contrib import admin

# Register your models here.

from appTpv.models import Factura, Articulo, Camarero, Periodo, Cantidad, Saldo

admin.site.register(Factura)

admin.site.register(Articulo)

admin.site.register(Camarero)

admin.site.register(Periodo)

admin.site.register(Cantidad)

admin.site.register(Saldo)
