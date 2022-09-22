from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    resposta = models.CharField(max_length=100)