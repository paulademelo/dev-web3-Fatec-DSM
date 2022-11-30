from django.shortcuts import render, redirect
from forms import CadastroForm
from .models import CadastroModel, PalestraModels


def index(request):
    palestras = PalestraModels.objects.all()
    palestras = {"palestras" : palestras}
    return render(request, 'index.html', palestras)

def cadastrar(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        # método para gravar
        if form.is_valid():
            form = CadastroForm()
            contexto = {"form": form}
            return render(request, 'form.html', contexto)
    else:
        # fluxo para exibir o formulário vazio GET
        form = CadastroForm()
        contexto = {'form' : form}
        return render(request, 'form.html', contexto)


def alunos_cadastrados(request):
    data = {}
    data['db'] = CadastroModel.objects.all()
    return render(request, 'alunos.html', data)            