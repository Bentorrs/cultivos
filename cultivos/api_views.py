from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Cultivo
from .serializers import CultivoSerializer

@api_view(['GET'])
def api_lista_cultivos(request):
    cultivos = Cultivo.objects.all()
    serializer = CultivoSerializer(cultivos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_agregar_cultivo(request):
    serializer = CultivoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_modificar_cultivo(request, pk):
    try:
        cultivo = Cultivo.objects.get(pk=pk)
    except Cultivo.DoesNotExist:
        return Response({'error':'Cultivo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CultivoSerializer(cultivo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
