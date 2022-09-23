from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('sair/', views.sair, name='sair'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('acesso/', views.acesso, name='acesso'),
    path('sistema/', views.sistema, name='sistema'),
    path('read/',  views.PessoaList.as_view() , name='exibir'),
    path('create/',  views.PessoaCreat.as_view() , name='criar'),
    path('update/<int:pk>/', views.PessoaUpdate.as_view(), name='atualizar'),
    path('delete/<int:pk>/', views.PessoaDelete.as_view(), name='deletar'),
]