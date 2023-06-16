from django.shortcuts import render
from PizzeríaApp.models import Pizzas, Ingredientes
# Create your views here.

def prueba(request):
    pizzas = Pizzas.objects.all()
    ingredientes = Ingredientes.objects.all()

    context = {
        'nombre': "Franco",
        'pizzas': pizzas,
        'ingredientes': ingredientes
    }

    return render(request, 'Test.html', context)

