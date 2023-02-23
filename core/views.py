from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


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
            messages.error(request, 'Usuario ou senha inválida.')
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):

    # evento = Evento.objects.get(id=1)
    # response = {'evento': evento}
    # return render(request, 'agenda.html', response)

    # evento = Evento.objects.all()
    # response = {'eventos': evento}
    # return render(request, 'agenda.html', response)

    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    # dados = {'eventos': evento}
    # return render(request, 'agenda.html', dados)

    # evento = Evento.objects.all()
    # dados = {'eventos': evento}
    # return render(request, 'agenda.html', dados)

    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

# from django.shortcuts import redirect
# def index(request):
#     return redirect('/agenda/')