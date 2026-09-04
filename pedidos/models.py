from django.db import models

class CategoriaIngrediente(models.Model):
    """Ex: Massas, Queijos, Molhos, Recheios"""
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria")

    class Meta:
        verbose_name = "Categoria de Ingrediente"
        verbose_name_plural = "Categorias de Ingredientes"

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    """Ex: Muçarela, Massa Integral, Cheddar, Bacon"""
    categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE, verbose_name="Categoria")
    nome = models.CharField(max_length=100, verbose_name="Nome do Ingrediente")
    preco_adicional = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, verbose_name="Preço Adicional (R$)")
    imagem = models.ImageField(upload_to='ingredientes/', blank=True, null=True, verbose_name="Foto do Ingrediente")

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return f"{self.nome} (+ R$ {self.preco_adicional})"
