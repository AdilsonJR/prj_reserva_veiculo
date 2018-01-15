import datetime
from django.db import models
from datetime import datetime

class Modelo(models.Model):

    def __str__(self):
        return self.modelo

    id_modelo = models.AutoField(max_length=20, primary_key=True)    
    modelo = models.CharField(max_length=200)

class Veiculo(models.Model):

    def __str__(self):
        return self.nome

    id_veiculo = models.AutoField(max_length=20, primary_key=True)    
    fk_modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    placa = models.CharField(max_length=200)
    nome = models.CharField(max_length=200) 
    data_fabricacao = models.DateField()
    estado = models.CharField(max_length=200)

class Funcionario(models.Model):
    
    def __str__(self):
        return self.nome 
    
    id_funcionario = models.AutoField(max_length=20, primary_key=True)    
    nome = models.CharField(max_length=200)
    veiculos = models.ManyToManyField(Veiculo, through='Reservas')
    
class Reservas(models.Model):
    
    def __str__(self):
        return 'data_reserva={0}, datadevolução={1}'.format(self.data_reserva, self.data_devolucao)
    
    fk_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    fk_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(default=datetime.now(), blank=None, null=None)
    data_devolucao = models.DateTimeField(default=datetime.now(), blank=None, null=None)

class Historico(models.Model):     

    def __str__(self):
        return self.data_reserva

    id_historico = models.AutoField(max_length=20, primary_key=True)
    fk_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(default=datetime.now(), blank=None, null=None)
    data_devolucao = models.DateTimeField(default=datetime.now(), blank=None, null=None)
    reservado_por = models.CharField(max_length=200)