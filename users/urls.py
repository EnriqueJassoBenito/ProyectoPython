from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

# Definir un router
router = SimpleRouter()
router.register(r'api',UserViewSet)

# ProductoViewset:
# ip:8000/productos/api/ <----- GET, POST de todo
# ip:8000/productos/api/{id} <----- GET, PUT, DELETE de uno

urlpatterns = [
    path('', include(router.urls)),
    # Este es el path para iniciar sesion
    # Es POST y espera que le mandemos email y password
    path('api/token/', CustomTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    # El siguiente path es para refrescar el token de sesion
    # (Si es que eso queremos porque podriamos iniciar sesion de nuevo simplemente)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='Token_refresh')
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