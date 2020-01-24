from rest_framework import generics
from computers.models import Computers
from .serializers import ComputersSerializer

class ComputersList(generics.ListCreateAPIView):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer

class ComputersDetail(generics.RetrieveUpdateAPIView):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer
