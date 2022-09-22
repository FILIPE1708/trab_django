from rest_framework import serializers
from tarefas.models.tarefa import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'resposta']