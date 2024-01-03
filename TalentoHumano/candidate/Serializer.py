from rest_framework import serializers
from .models import Candidato

class CandidatoSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    correo = serializers.EmailField()
    fecha_nacimiento = serializers.DateField()

    telefono = serializers.CharField(max_length=20, allow_blank=True, allow_null=True)
    direccion = serializers.CharField(allow_blank=True, allow_null=True)
    experiencia_laboral = serializers.CharField(allow_blank=True, allow_null=True)
    habilidades = serializers.CharField(allow_blank=True, allow_null=True)
    fecha_entrevista = serializers.DateTimeField(allow_null=True)

    def create(self, validated_data):
        return Candidato.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Actualiza la instancia de Candidato existente con los nuevos datos
        instance.nombre = validated_data.get('nombre', instance.nombre)
        # Actualiza otros campos aquí
        instance.save()
        return instance
