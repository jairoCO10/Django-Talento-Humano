from .models import Candidato


class CandidateService:
    def __init__(self) -> None:
        pass

    def _get_byid_(self, iduuid):
        response = Candidato.objects.get(id = iduuid)
        return response
        

    def delete_candidate(self,candidate_data, candidate):
        candidate_data.delete()
        return True
    
    
    def _update_candidate(self, candidate_data):
        candidate_data.save()
        return True
       

