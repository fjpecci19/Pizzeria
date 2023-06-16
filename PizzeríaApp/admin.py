from django.contrib import admin
from .models import Pizzas, Ingredientes
# Register your models here.

@admin.register(Pizzas)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')


@admin.register(Ingredientes)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
