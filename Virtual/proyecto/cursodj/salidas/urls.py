from django.urls import path

from salidas.views import FacturaList

urlpatterns = [
     path("facturas", FacturaList().as_view(), name="factura_list")
]
