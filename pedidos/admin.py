from django.contrib import admin
from .models import CategoriaIngrediente, Ingrediente

@admin.register(CategoriaIngrediente)
class CategoriaIngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco_adicional')
    list_filter = ('categoria',)
    search_fields = ('nome',)
