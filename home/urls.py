from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cadastrar/', views.cad_user, name='user'),
    path('login/', views.login_user, name='login'),
    path('reserva/', views.reserva, name='reserva'),

]