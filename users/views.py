from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.renderers import JSONRenderer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]
    
    # Como le pongo seguridad?
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Sobreescribir el metodo para la obtencion de permisos
    def get_permissions(self):
        if self.request.method in ['POST','PUT','DELETE']:
            # Checar si tenemos sesion
            return [IsAuthenticated()]
        # Dar acceso a todo lo demas sin estar logueando
        return[]
    
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer