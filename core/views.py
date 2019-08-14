from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.

def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos. </h1>' .format(nome, idade))

def eventos(request,titulo_evento):
    # evento = Evento()
    # Evento.objetcs.get(titulo = titulo_evento)
    return HttpResponse('<h2>O evento marcado é: {}. </h2>' .format(titulo_evento))

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all() #filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)