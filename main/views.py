from django.shortcuts import render
from pessoas.models import Pessoa
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
#from .models import Post

class CrudIndex(ListView):
    model = Pessoa
    template_name = 'main/index.html'