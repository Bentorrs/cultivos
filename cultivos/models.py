from django.db import models

# Zona con Cultivo en una relacion 1 : N
class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
# Un cultivo puede tener muchas plagas y esa plaga puede estar en muchos cultivos N : M
class Plaga(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
# La clase Cultivo que es el modelo principal donde colocaremos las relaciones de 1 : N y N : M
class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    siembra = models.CharField(max_length=100)
    cosecha = models.CharField(max_length=100)

    # Relacionamos 1 : N con Zona
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="cultivos")

    # Relacionamos N : M con Plaga
    plagas = models.ManyToManyField(Plaga, blank=True, related_name="cultivos")

    def __str__(self):
        return self.nombre
    
# Relacion 1 : 1 entre Ficha técnica con Cultivo
class FichaTecnica(models.Model):
    cultivo = models.OneToOneField(Cultivo, on_delete=models.CASCADE, related_name="ficha")
    requerimientos = models.TextField()
    cuidados = models.TextField()
    fertilizantes_recomendados = models.TextField()

    def __str__(self):
        return f"Ficha de {self.cultivo.nombre}"