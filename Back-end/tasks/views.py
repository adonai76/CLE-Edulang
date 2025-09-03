from rest_framework import viewsets
from .serializer import AlumnoSerializer
from .models import Alumno 

# Create your views here.
class AlumnoViewSet(viewsets.ModelViewSet):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()

