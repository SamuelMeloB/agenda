from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank = True, null=True)
    local = models.TextField(blank = True, null=True)
    data_evento = models.DateTimeField(verbose_name= 'Data do Evento')
    data_criacao = models.DateTimeField(auto_now = True, verbose_name= 'Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #se o usuario for excluido, todos os seus eventos tbm serao

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo #sempre que for chamado ele vai trazer o nome do titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%Mhs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M') #um espaço faz bastante diferenca

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False