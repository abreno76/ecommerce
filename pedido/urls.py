from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'pedido'

urlpatterns = [
    path('pagar/', views.Pagar.as_view(), name='pagar'),
    path('fecharpedido/', views.FecharPedido.as_view(), name='fecharpedido'),
    path('detalhe/int:pk', views.Detalhe.as_view(), name='detalhe'),
]