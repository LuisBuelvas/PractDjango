from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FacturaDet, FacturaEnc
from generales.views import SinPrivilegios
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class FacturaList(LoginRequiredMixin, generic.ListView):
    login_url = 'generales:login'
    model = FacturaEnc
    template_name = "salidas/facturas_list.html"
    context_object_name = "facturas"