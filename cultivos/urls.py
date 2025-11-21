from django.urls import path
from .views import listar_cultivos, detalle_cultivo, registrar_cultivo
from .api_views import api_lista_cultivos, api_agregar_cultivo, api_modificar_cultivo

urlpatterns = [
    path('', listar_cultivos, name='listar_cultivos'),
    path('agregar/', registrar_cultivo, name='registrar_cultivo'),
    path('detalle/<str:nombre>/', detalle_cultivo, name='detalle_cultivo'),
    path('api/cultivos/', api_lista_cultivos, name='api_lista_cultivos'),
    path('api/cultivos/agregar', api_agregar_cultivo, name='api_agregar_cultivos'),
    path('api/cultivos/<int:pk>/modificar', api_modificar_cultivo, name='api_modificar_cultivos'),
]
