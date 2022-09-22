from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from tarefas.models.tarefa import Tarefa
from tarefas.serializer.tarefa_serializer import TarefaSerializer

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
