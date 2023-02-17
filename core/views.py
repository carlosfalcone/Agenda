from django.shortcuts import render
from core.models import Evento

# Create your views here.

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

    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


# from django.shortcuts import redirect
# def index(request):
#     return redirect('/agenda/')