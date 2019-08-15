from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime,timedelta
from django.http.response import Http404, JsonResponse

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
    data_atual = datetime.now() - timedelta(hours=1)        #se quiser que apareça todos, retira data_evento do filter
    data_1depois = datetime.now() + timedelta(hours=1) #    data_evento__gt=data_atual, data_evento__lt=data_1depois
    evento = Evento.objects.filter(usuario=usuario) #filter(usuario=usuario) #__gt eh depois da data e __lt eh antes da data
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    print(id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        usuario = request.user
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        id_evento = request.POST.get('id_evento')
        local = request.POST.get('local')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.local = local
                evento.save()
            # Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                       data_evento=data_evento,
            #                       descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  local=local,
                                  usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento =Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

def json_lista_evento(request,id_usuario): #nao instancie dentro do login senao buga
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id','titulo') #filter(usuario=usuario) #__gt eh depois da data e __lt eh antes da data
    return JsonResponse(list(evento),safe=False) #ou {{'titulo':'teste'}}

