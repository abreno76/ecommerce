from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View


class ListaProduto(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista Produto')


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe produto')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao carrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
