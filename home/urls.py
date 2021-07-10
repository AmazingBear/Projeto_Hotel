from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('cadastrar/', views.cad_user, name='user'),
    path('formulario', views.insere_cliente, name='insere_cliente'),
    path('reserva/', views.reserva, name='reserva'),
    path('cad_reserva/', views.insere_reserva, name='insere_reserva'),
    path('cliente/', views.cliente, name='cliente'),
    path('hoteis_reservados/', views.hoteis_reservados, name='hoteis_reservados'),
]