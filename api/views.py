from rest_framework import viewsets
from .models import Ariza, Savol, Kurs, Natija, SavolJavob
from .serializers import ArizaSerializer, SavolSerializer, KursSerializer, NatijaSerializer, SavolJavobSerializer

class ArizaViewSet(viewsets.ModelViewSet):
    queryset = Ariza.objects.all().order_by('-id')
    serializer_class = ArizaSerializer

class SavolViewSet(viewsets.ModelViewSet):
    queryset = Savol.objects.all().order_by('-id')
    serializer_class = SavolSerializer

class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer

class NatijaViewSet(viewsets.ModelViewSet):
    queryset = Natija.objects.all()
    serializer_class = NatijaSerializer

class SavolJavobViewSet(viewsets.ModelViewSet):
    queryset = SavolJavob.objects.all()
    serializer_class = SavolJavobSerializer