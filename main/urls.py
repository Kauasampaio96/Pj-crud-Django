from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrudIndex.as_view(), name='index'),
]