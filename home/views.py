from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def cad_user(request):
    return render(request, 'home/cad_user.html')

def login_user(request):
    return render(request, 'home/login_user.html')

def reserva(request):
    return render(request, 'home/reserva.html')