from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cultivo
from .serializers import CultivoSerializer

@api_view(['GET'])
def api_lista_cultivos(request):
    cultivos = Cultivo.objects.all()
    serializer = CultivoSerializer(cultivos, many=True)
    return Response(serializer.data)