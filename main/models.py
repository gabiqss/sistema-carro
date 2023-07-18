from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length = 30)
    marca = models.CharField(max_length = 30)
    ano = models.IntegerField()
    cor = models.CharField(max_length = 15)
 
    def __str__(self):
        return self.modelo
    
