from rest_framework import serializers
from .models import Cultivo, Zona, Plaga

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = ['id', 'descripcion']

class PlagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plaga
        fields = ['id', 'descripcion']

class CultivoSerializer(serializers.ModelSerializer):
    zona = ZonaSerializer
    plaga = PlagaSerializer
    class Meta:
        model = Cultivo
        fields = ['id', 'nombre', 'tipo','siembra',
                    'cosecha', 'zona', 'plagas']
        
