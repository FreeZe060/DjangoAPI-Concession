from rest_framework import viewsets
from .models import Concession, Vehicule
from .serializers import ConcessionSerializer, VehiculeSerializer

class ConcessionViewSet(viewsets.ModelViewSet):
    queryset = Concession.objects.all()
    serializer_class = ConcessionSerializer


class VehiculeViewSet(viewsets.ModelViewSet):
    serializer_class = VehiculeSerializer

    def get_queryset(self):
        concession_id = self.kwargs.get('concession_pk')
        return Vehicule.objects.filter(concession_id=concession_id)
