from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos. </h1>' .format(nome, idade))

def eventos(request,titulo_evento):
    # evento = Evento()
    # Evento.objetcs.get(titulo = titulo_evento)
    return HttpResponse('<h2>O evento marcado é: {}. </h2>' .format(titulo_evento))

def index(request):
    return redirect('/agenda/')

def login_user(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username = username,password = password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido.")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request): #nao instancie dentro do login senao buga
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) #filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)