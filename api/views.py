from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ariza, Savol, Kurs, Natija, SavolJavob
from .serializers import ArizaSerializer, SavolSerializer, KursSerializer, NatijaSerializer, SavolJavobSerializer

class ArizaViewSet(viewsets.ModelViewSet):
    queryset = Ariza.objects.all().order_by('-id')
    serializer_class = ArizaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ism', 'telefon']

class SavolViewSet(viewsets.ModelViewSet):
    queryset = Savol.objects.all().order_by('-id')
    serializer_class = SavolSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['matn']

class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nomi']

class NatijaViewSet(viewsets.ModelViewSet):
    queryset = Natija.objects.all()
    serializer_class = NatijaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

class SavolJavobViewSet(viewsets.ModelViewSet):
    queryset = SavolJavob.objects.all()
    serializer_class = SavolJavobSerializer
    filter_backends = [DjangoFilterBackend]