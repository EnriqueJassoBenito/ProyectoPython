from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Alumno
from .serializer import AlumnoSerializer
from .forms import alumnoForms
from django.shortcuts import render, redirect

class AlumnoViewset(viewsets.ModelViewSet):
    # Conjunto de query's de la BD
    queryset = Alumno.objects.all()

    # Saber como empaquetar e enviar la informacion
    serializer_class = AlumnoSerializer

    # Saber como voy a renderizar las respuestas
    renderer_classes = [JSONRenderer]
    
def alumno_list(request):
    form = alumnoForms()
    return render(request, 'osorio_enrique.html', {'form': form})

# def alumno_list(request):
#     if request.method == 'POST':
#         form = alumnoForms(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('alumno_list')  # Redirige a la lista después de guardar
#     else:
#         form = alumnoForms()

#     alumnos = Alumno.objects.all()
#     return render(request, 'osorio_enrique.html', {'form': form, 'alumnos': alumnos})