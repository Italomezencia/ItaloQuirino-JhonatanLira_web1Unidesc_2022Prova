from django.db import models

class Contrato(models.Model):

    dadosCliente = models.CharField(max_length=100)
    dadosCorretor = models.CharField(max_length=100)
    descricaoImovel = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    documentacao = models.CharField(max_length=100)
    clausulaPenal = models.CharField(max_length=100)

def __str__(self):
    return self.nome