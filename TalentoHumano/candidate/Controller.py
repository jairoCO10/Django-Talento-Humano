from .Service import CandidateService
from rest_framework import status
from rest_framework.response import Response


class CandidateController:
    def __init__(self):
        self.candidate = CandidateService()
        


    def _get_byid_(self, iduuid):

        response = self.candidate._get_byid_(iduuid)

        if not response:
            raise Response(
                status=status.HTTP_404_NOT_FOUND
            )
        return self.procesar_usuario(response)
    

    def delete_candidate_by_uuid(self, iduuid):
        candidate_data = self.candidate._get_byid_(iduuid)
        if not candidate_data:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = self.candidate.delete_candidate(candidate_data,iduuid)
        if response:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_409_CONFLICT)
    
    def update_candidate(self,request_data, iduuid):

        print(request_data)
        candidate_data = self.candidate._get_byid_(iduuid)

        if not candidate_data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Actualiza los campos del objeto Candidato con los datos recibidos
        candidate_data.nombre = request_data["nombre"]
        candidate_data.apellido = request_data["apellido"]
        # Otros campos que necesites actualizar...

        actualizacion_exitosa = self.candidate._update_candidate(candidate_data)
      
        if actualizacion_exitosa:  # Si la actualización fue exitosa
            return Response({'message': 'Actualización exitosa'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Error en la actualización'}, status=status.HTTP_409_CONFLICT)

    
    def procesar_usuario(self, response):
        campos = [  
                    'id', "nombre", "apellido"
                ]
        return self.data_procesada(campos, response)

    def data_procesada(self, campos, response):
        procesado = {}
        for campo in campos:
            value = getattr(response, campo)
            if value is None:
                value = 'N/A'
                procesado[campo] = value
            else:
                procesado[campo] = value

        return procesado