from rest_framework.serializers import ModelSerializer
from .models import Alumno

class AlumnoSerializer(ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'
