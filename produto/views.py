from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models


class ListaProduto(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):

        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('produto:lista'))
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto não existe',
            )
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        if variacao_id in self.request.session['carrinho']:
            # TODO: Variação existe no carrinho
            ...
        else:
            # TODO: Varação não existe no carrinho
            ...

        return HttpResponse(f'{variacao.produto} {variacao.nome}')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
