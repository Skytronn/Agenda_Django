from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from django.http.response import Http404
from django.http import JsonResponse

## Abaixo pode se fazer o redirecionamento do index para a agenda
#def index(request):
#    return redirect('/agenda')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalido")
    return redirect('/')

#Quando o usuario não estiver autenticado, irá direcionar para este url

def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() # - timedelta(hour=1) esta função irá pegar eventos até uma hora antes de vencer
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__lt=data_atual)#__gt para eventos que não passaram e __lt para eventos que ja passaram
    dados = {'eventos':evento}

    return render(request, 'agenda.html', dados)

def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()

#Este update abaixo tambem serve, porem o de cima tem a segurança contra updates atraves da url
  #         Evento.objects.filter(id=id_evento).update(titulo=titulo,
  #                                                     data_evento=data_evento,
  #                                                     descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)

    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


@login_required(login_url='/login/')
def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento),safe=False)