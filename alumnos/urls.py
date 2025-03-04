from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewset
from .views import *
from .templates import *

# Definir un router
router = SimpleRouter()
router.register(r'api',AlumnoViewset)

# ProductoViewset:
# ip:8000/productos/api/ <----- GET de todo
# ip:8000/productos/api/{id} <----- GET, POST, PUT, DELETE de uno

urlpatterns = [
    path('', include(router.urls)),
    path('alumno_list/', alumno_list, name='alumno_list'),  # Página HTML
]


