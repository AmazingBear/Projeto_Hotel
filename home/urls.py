from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cadastrar/', views.cad_user, name='user'),
    path('formulario', views.insere_cliente, name='insere_cliente'),
    path('login/', views.login_user, name='login'),
    path('reserva/', views.reserva, name='reserva'),
    path('cliente/', views.cliente, name='cliente'),
]