from rest_framework import viewsets
from .models import Concession, Vehicule
from .serializers import ConcessionSerializer, VehiculeSerializer

class ConcessionViewSet(viewsets.ModelViewSet):
    queryset = Concession.objects.all()
    serializer_class = ConcessionSerializer


class VehiculeViewSet(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer
