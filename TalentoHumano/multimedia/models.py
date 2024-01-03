from django.db import models
import uuid
from candidate.models import Candidato

class FotoCandidato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

    
    imagen = models.ImageField(upload_to='fotos_candidatos/')
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.candidato.nombre} {self.candidato.apellido}"
