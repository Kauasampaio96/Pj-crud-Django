from django.contrib import admin
from pessoas.models import Pessoa

# Register your models here.
'''class PessoaAdmin(admin.ModelAdmin):
    model = Pessoa
    list_display = ['nome', 'data_nasc', 'telefone', 'estado', 'cpf']
    
    
admin.site.register(Pessoa, PessoaAdmin)'''