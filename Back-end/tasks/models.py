from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_carrera = models.CharField(max_length=255, unique=True)
    plan_estudios_carrera = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # timestamps()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_carrera


class Nivel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_nivel = models.CharField(max_length=255)
    mcr_nivel = models.CharField(max_length=10)
    horas_nivel = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # timestamps()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_nivel} ({self.mcr_nivel})"


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con usuarios
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    matricula_alumno = models.CharField(max_length=20, unique=True)
    nombre_alumno = models.CharField(max_length=100)
    apellidos_alumno = models.CharField(max_length=100)
    edad_alumno = models.PositiveSmallIntegerField()
    sexo_alumno = models.CharField(max_length=50)
    semestre_alumno = models.PositiveSmallIntegerField()

    inscrito = models.BooleanField(default=False)
    acredita = models.BooleanField(default=False)
    liberado = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)  # equivalente a timestamps()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_alumno} {self.apellidos_alumno} - {self.matricula_alumno}"
