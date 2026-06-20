from rest_framework import serializers
from .models import Ariza, Savol, Kurs, Natija, SavolJavob

class ArizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ariza
        fields = '__all__'

class SavolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savol
        fields = '__all__'

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = '__all__'

class NatijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natija
        fields = '__all__'

class SavolJavobSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SavolJavob
        fields = '__all__'