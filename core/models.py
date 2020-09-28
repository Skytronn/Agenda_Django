from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Criação do meu objeto/tabela de migração para o bd

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #Nomeando a tabela como "evento"
    class Meta:
        db_table = 'evento'

    #função para carregar titulo automaticamente na pagina do admin do django
    def __str__(self):
        return self.titulo

    #Alteração do tipo da data que vem do banco
    def get_data_criacao(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%d')