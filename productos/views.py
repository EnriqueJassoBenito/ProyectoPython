from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Producto
from .serializer import ProductoSerializer
from .forms import productoForm

def agregar(request):
    form = productoForm()
    return render(request, 'agregar.html',{'form':form}, status=200)

class ProductoViewset(viewsets.ModelViewSet):
    # Conjunto de query's de la BD
    queryset = Producto.objects.all()

    # Saber como empaquetar e enviar la informacion
    serializer_class = ProductoSerializer

    # Saber como voy a renderizar las respuestas
    renderer_classes = [JSONRenderer]








# from django.shortcuts import render, redirect
# from .models import Producto
# from .forms import productoForm
# from django.http import JsonResponse

# # Create your views here.
# def agregar_producto(request):
#     # Checar si vengo desde el formulario enviado
#     if request.method == 'POST':
#         # Mandaron el formulario
#         form = productoForm(request.POST)
#         # validar que el formulario este correcto
#         if form.is_valid():
#             # Si es valido entonces lo guardo
#             form.save()
#             return redirect('ver') # Redirecciona a la lista productos
        
#     # Si no vengo de enviar el formulario (si solo lo quiero ver)            
#     else:
#         form = productoForm()
        
#     # vamos a pintar el formulario
#     return render(request, 'agregar.html', {'form': form})
        
# # Funcion que agrega producto desde una llamada asincrona
# import json
# # etiqueta para evitar el uso de CSRF
# # @csrf_exempt <--- evitar su uso a menos que estemos probando
# def registrar_producto(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body) # funcion que toma texto crudo y lo convierte en JSON
#             producto = Producto.objects.create(
#                 nombre=data['nombre'],
#                 precio=data['precio'],
#                 imagen=data['imagen']
#             ) # Estamos construyendo la instancia y guardandola en la BD
#             return JsonResponse({
#                 'mensaje': 'Registro exitoso, felicidades!',
#                 'id': producto.id
                
#             }, status = 201)
#         except Exception as e:
#             return JsonResponse({
#                 'Error': 'ocurrio un error:' + str(e)
#             }, status=400)
#     return JsonResponse({
#         'Error': 'Metodo no soportado'
#     }, status = 405)
        
# def ver_producto(request):
#     # Obtener de la BD todo los productos
#     productos = Producto.objects.all()
#     return render(request, 'ver.html', {'productos':productos})

# # Esta funcion pinta el HTMl que carga los productos con JSON
# def index(request):
#     return render(request, 'productos.html')

# # Esta otra funcion que devuelve todos los productos como un JSON
# def lista_productos(request):
#     productos = Producto.objects.all()
    
#     # generar un diccionario al aire que ordene los productos
#     data = [
#         {
#             'nombre': p.nombre,
#             'precio': p.precio,
#             'imagen': p.imagen
#         }
#         for p in productos
#     ]
    
#     return JsonResponse(data, safe=False)


    