#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello' ),
    path('details/<int:pk>/', views.product_detail, name='product_detail'),
    path('newproduct/', views.new_product, name='new_product'),
    #path('saludo/', views.saludo, name='saludo')
]
