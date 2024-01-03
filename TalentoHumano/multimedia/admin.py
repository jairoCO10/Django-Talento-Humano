from django.contrib import admin
from .models import FotoCandidato


@admin.register(FotoCandidato)
class ImagenCandidato(admin.ModelAdmin):
    list_display = ('id', 'imagen',"candidato" )
    list_filter = ('fecha_subida',)
