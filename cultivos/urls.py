from django.urls import path
from .views import listar_cultivos, detalle_cultivo, registrar_cultivo
from .api_views import api_lista_cultivos

urlpatterns = [
    path('', listar_cultivos, name='listar_cultivos'),
    path('agregar/', registrar_cultivo, name='registrar_cultivo'),
    path('detalle/<str:nombre>/', detalle_cultivo, name='detalle_cultivo'),
    path('api/cultivos/', api_lista_cultivos, name='api_lista_cultivos')
]
