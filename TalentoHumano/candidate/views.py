from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Candidato
from multimedia.models import FotoCandidato
from .Serializer import CandidatoSerializer
from .Controller import CandidateController




@api_view(['GET', 'POST'])
def candidato_list(request):
    if request.method == 'GET':
        candidatos = Candidato.objects.all()
        serializer = CandidatoSerializer(candidatos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CandidatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def candidato_detail(request, iduuid):
    try:
        candidato = CandidateController()
        print(iduuid)
        response = candidato._get_byid_(iduuid)

    except Candidato.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        return Response(response)
    
   
@api_view(['DELETE'])
def candidato_delete(request, iduuid):
    try:
        candidato_controller = CandidateController()
        response_delete = candidato_controller.delete_candidate_by_uuid(iduuid)
        return response_delete

    except Candidato.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def candidato_update(request, iduuid):
    request_data = request.data
    print(request_data["nombre"])  # Imprime los datos de la solicitud en la consola
        # Realizar otras operaciones con los datos según sea necesario
    

    try:
        candidato_controller = CandidateController()
        response_update = candidato_controller.update_candidate(request_data,iduuid)
        return Response(response_update)

    except Candidato.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



    # if request.method == 'GET':
    #     candidato_data = {
    #         'id': candidato.id,
    #         'nombre': candidato.nombre,
    #         'apellido': candidato.apellido,
    #         'correo': candidato.correo,
    #         # Añade los demás campos del modelo 'Candidato' que necesites aquí...
    #         'foto': None
    #     }
    #     # candidato_data["id"] =candidato.id

    #     # Obtener el primer objeto si existe en el queryset 'foto_candidato'
    #     primer_foto_candidato = foto_candidato.first()  # O .last() dependiendo de tus necesidades

    #     if primer_foto_candidato:
    #         candidato_data['foto'] = {
    #             'id': primer_foto_candidato.id,
    #             'imagen': primer_foto_candidato.imagen.url if primer_foto_candidato.imagen else None,
    #             'descripcion': primer_foto_candidato.descripcion,
    #             # Añade otros campos de 'FotoCandidato' que necesites aquí...
    #         }

    #     return Response(candidato_data)


    # elif request.method == 'PUT':
    #     serializer = CandidatoSerializer(candidato, data=request.data)
    #     if serializer.is_valid():
    #         serializer.
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     candidato.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
