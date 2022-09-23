from django.db import models
from cpf_field.models import CPFField



class Pessoa(models.Model):
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("BA", "Bahia"),
        ("CE", "Ceara"),
        ("DF", "Distrito Federal"),
        ("ES", "Espirito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
        
    )
    
    
    
    
    nome = models.CharField(max_length=255, verbose_name='Nome',)
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    telefone = models.CharField(max_length=255, verbose_name='Telefone', blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, verbose_name='Estado', blank=True)
    #cpf = models.CharField(max_length=14, verbose_name='Cpf')
    cpf = CPFField(verbose_name='Cpf', max_length=14)
    
    def __str__(self):
        return self.nome
