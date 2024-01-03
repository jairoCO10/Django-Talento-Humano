from django.db import models
import uuid


class Candidato(models.Model):
    # Información básica del candidato
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    
    # Información adicional (opcional)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True) 
    # Información sobre el proceso de selección
    experiencia_laboral = models.TextField(blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    fecha_entrevista = models.DateTimeField(blank=True, null=True)
    
    # Otras relaciones o campos según necesidades específicas
    # ...

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
