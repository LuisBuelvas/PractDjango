from django.db import models
from generales.models import ClaseModelo
from decimal import Decimal

from catalogos.models import Producto

# Create your models here.

class FacturaEnc(ClaseModelo):
    fecha_factura = models.DateField()
    observacion = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.fecha_factura)
    
    class Meta:
        verbose_name_plural = "Encabezado de Facturas"
        verbose_name = "Encabezado de Factura"


class FacturaDet(ClaseModelo):
    factura = models.ForeignKey(FacturaEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    def __str__(self):
        return '{}'.format(self.factura, self.producto)
    
    def save(self):
        self.total = Decimal(self.cantidad) * Decimal(self.precio)
        super(FacturaDet,self).save()
    
    class Meta:
        verbose_name_plural = "Detalles de Facturas"
        verbose_name = "Detalle de Factura"
