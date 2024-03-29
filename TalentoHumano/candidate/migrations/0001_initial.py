# Generated by Django 4.2.8 on 2023-12-26 17:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('experiencia_laboral', models.TextField(blank=True, null=True)),
                ('habilidades', models.TextField(blank=True, null=True)),
                ('fecha_entrevista', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
