from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class FecharPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar Pedido')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
