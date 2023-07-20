from pathlib import Path

from django.conf import settings
from django.db import models
from PIL import Image


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produtos_imagem/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(max_length=1,
                            default='V',
                            choices=(('V', 'Variação'),
                                     ('S', 'Simples'),))

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            resize_image(self.imagem)


@staticmethod
def resize_image(img, new_width=800):
    image_path = Path(settings.MEDIA_ROOT, img.name)
    # print(image_path)
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    if original_width <= new_width:
        image_pillow.close()
        return image_pillow

    new_height = round((new_width * original_height) / original_width)

    new_imagem = image_pillow.resize((new_width, new_height), Image.LANCZOS)

    new_imagem.save(
        image_path,
        optimize=True,
        quality=60,
    )

    return new_imagem


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
