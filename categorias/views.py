from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse

# Create your views here.

def agregar_categoria(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
        
    else:
        form = categoriaForm()
        
    return render(request, 'agregarCategorias.html', {'form': form})

import json
def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            categoria = Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Registro exitoso, felicidades!',
                'id': categoria.id
            }, status = 201)
        except Exception as e:
            return JsonResponse({
                'Error': 'ocurrio un error:' + str(e)
            }, status = 400)

def ver_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'ver-categoria.html', {'categorias':categorias})

def index(request):
    return render(request, 'categorias.html')

def lista_categoria(request):
    categorias = Categoria.objects.all()
    
    # generar un diccionario al aire que ordene los productos
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]
    
    return JsonResponse(data, safe=False)
