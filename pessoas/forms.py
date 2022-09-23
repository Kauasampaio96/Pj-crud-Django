from django import forms

from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder': 'Um Nome'})
        self.fields['data_nasc'].widget.attrs.update({'class': 'mask-data', 'placeholder': 'Uma Data'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone', 'placeholder': 'Um Telefone'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf', 'placeholder': 'Um CPF'})
        
        
        
        