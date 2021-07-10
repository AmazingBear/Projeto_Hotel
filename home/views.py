from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import conexao
from django.contrib.auth.models import User



__login = True

con = conexao.conectar()
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def cad_user(request):
    return render(request, 'home/cad_user.html')

def insere_cliente(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    telefone = request.POST.get('telefone')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    with con.cursor() as inserir:
        sql = 'insert into tbcliente(nome, idade, telefone, cpf, email, senha) values(%s, %s, %s, %s, %s, %s)'
        inserir.execute(sql, (nome, idade, telefone, cpf, email, senha))
        con.commit()
    return render(request, 'home/cad_user.html')

def reserva(request):
    return render(request, 'home/reserva.html')

def insere_reserva(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    hotel = request.POST.get('hotel')
    dias_reservados = request.POST.get('dias_reservados')
    num_quartos = request.POST.get('num_quartos')
    num_adultos = request.POST.get('num_adultos')
    num_criancas = request.POST.get('num_criancas')

    with con.cursor() as inserir:
        sql = 'insert into tbreserva(nome, cpf, telefone, hotel, dias_reservados, num_quartos, num_adultos, num_criancas) ' \
              'values(%s, %s, %s, %s, %s, %s, %s, %s)'
        inserir.execute(sql, (nome, cpf, telefone, hotel, dias_reservados, num_quartos, num_adultos, num_criancas))
        con.commit()
    return render(request, 'home/reserva.html')


def cliente(request):
    if __login == True:
        with con.cursor() as selecionar:
            sql = 'select * from tbcliente'
            selecionar.execute(sql)
            dados = selecionar.fetchall()
        return render(request, 'home/cliente.html', {'clientes':dados})
    else:
        return render(request, 'home/cliente.html')

def hoteis_reservados(request):
    if __login == True:
        with con.cursor() as selecionar:
            sql = 'select * from tbreserva'
            selecionar.execute(sql)
            dados = selecionar.fetchall()
        return render(request, 'home/hoteis_reservados.html', {'hoteis':dados})
    else:
        return render(request, 'home/hoteis_reservados.html')