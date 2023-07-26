from django.contrib import admin

from . import models


class VariacaoInLine(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta',
                    'get_preco_marketing_formatado',
                    'get_preco_marketing_promocional_formatado']
    inlines = [
        VariacaoInLine
    ]


"""
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produtos_imagem/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
"""

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
