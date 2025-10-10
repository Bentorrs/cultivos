from django.contrib import admin
from .models import Cultivo, Zona, Plaga, FichaTecnica

admin.site.register(Cultivo)
admin.site.register(Zona)
admin.site.register(Plaga)
admin.site.register(FichaTecnica)
