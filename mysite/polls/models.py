import datetime

from django.db import models
from django.utils import timezone

class Pregunta(models.Model):
    textoPregunta = models.CharField(max_length=250)
    fechaPublicacion = models.DateTimeField('date published')
    def __str__(self):
        return self.textoPregunta
    def reciente(self):
        return self.fechaPublicacion >= timezone.now() - datetime.timedelta(days=1)

class Eleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    textoEleccion = models.CharField(max_length=250)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.textoEleccion


