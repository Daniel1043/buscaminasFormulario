from django.db import models

class MiModelo(models.Model):
    indice_fila = models.IntegerField()
    indice_columna = models.IntegerField()