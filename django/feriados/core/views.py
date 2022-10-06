from asyncore import dispatcher_with_send
from django.shortcuts import render
from datetime import datetime
from .models import FeriadoModel
from .forms import FeriadoForm

def verifica_feriado(request):
    hoje = datetime.today()
    resultado = FeriadoModel.objects.filter(dia=hoje.day).filter(mes=hoje.month)
    if len(resultado) > 0:
        contexto = {'feriado': True, 'nome': resultado[0].nome}
    else:
        contexto = {'feriado': False}
    return render(request, 'feriado.html', contexto)

def cadastrar(request):
    if request.method == 'POST':
        # método para gravar
        form = FeriadoForm(request.POST)
        if form.is_valid():
            contexto = {}
            return render(request, 'Feriado.html', contexto)
        else:
            contexto = {'form', form}
            return render(request, 'Feriado.html', contexto)

    else:
        # fluxo para exibir o formulário vazio GET
        form = FeriadoForm()
        contexto = {'form' : form}
        return render(request, 'cadastrar.hmtl', contexto)
