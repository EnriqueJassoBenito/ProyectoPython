from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductoViewset
from .views import *

# Definir un router
router = SimpleRouter()
router.register(r'api',ProductoViewset)

# ProductoViewset:
# ip:8000/productos/api/ <----- GET de todo
# ip:8000/productos/api/{id} <----- GET, POST, PUT, DELETE de uno

urlpatterns = [
    path('', include(router.urls)),
    path('agregar/', agregar, name = 'agregar')
]




# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('agregar/', agregar_producto, name='agregar'),
#     path('ver/', ver_producto, name='ver'),
#     path('', index, name='home'),
#     path('api/get/', lista_productos, name='lista'),
#     path('api/post/', registrar_producto, name='post')
# ]