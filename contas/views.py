from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pessoas.models import Pessoa
from pessoas.forms import PessoaForm

def login(request):
    
    
    if request.user.is_authenticated:
        return redirect('sistema')
    
    
    if request.method != 'POST':
       return render(request, 'login.html') 
   
    usuario= request.POST.get('usuario')
    senha= request.POST.get('senha')
    
    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou Senha inválidos')
        return render(request, 'login.html')
    
    else:
        auth.login(request, user)
        return redirect ('acesso')        
   

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'cadastro.html')
    
    
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    
    if not usuario or not email or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'cadastro.html')
    
    
    
    try:
        validate_email(email)
        
    except:
        messages.error(request, 'E-mail inválido.')
        return render(request, 'cadastro.html')
    
    
    if senha != senha2:
        messages.warning(request, 'As senhas não correspondem.')
        return render(request, 'cadastro.html')
    
    if len(senha) < 7:
        messages.warning(request, 'Senha muito curta.')
        return render(request, 'cadastro.html')
    
    if len(usuario) < 7:
        messages.warning(request, 'Nome de usuário muito curto.')
        return render(request, 'cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'cadastro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'cadastro.html')
    
    messages.success(request, 'Cadastro Efetuado com Sucesso, Faça Login!')
    user= User.objects.create_user(username=usuario, email=email, password=senha)
    user.save()
    return redirect('index_login')




@login_required(redirect_field_name='index_login')
def acesso(request):
    return render(request, 'acesso.html')


@login_required(redirect_field_name='index_login')
def sair(request):
    auth.logout(request)
    return render(request, 'logout.html')


@login_required(redirect_field_name='index_login')
def sistema(request):
    return render(request, 'sistema.html')


class PessoaList(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all()
    template_name = 'read.html'
    
    
class PessoaCreat(CreateView):
    form_class = PessoaForm        
    template_name ='create.html'
    success_url = reverse_lazy('exibir')
    

class PessoaUpdate(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'update.html'
    success_url = reverse_lazy('exibir')
    
class PessoaDelete(DeleteView):
    queryset = Pessoa.objects.all()
    template_name = 'pessoa_confirm_delete.html'
    success_url = reverse_lazy('exibir')