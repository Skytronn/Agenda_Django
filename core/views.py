from django.shortcuts import render,redirect
from core.models import Evento

## Abaixo pode se fazer o redirecionamento do index para a agenda
#def index(request):
#    return redirect('/agenda')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos':evento}

    return render(request, 'agenda.html', dados)