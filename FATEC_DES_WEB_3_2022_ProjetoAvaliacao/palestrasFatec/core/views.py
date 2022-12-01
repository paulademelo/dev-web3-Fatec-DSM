from django.shortcuts import render
from forms import CadastroForm
from .models import CadastroModel


def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        # método para gravar
        if form.is_valid():
            CadastroModel.objects.create(**form.cleaned_data)
            form = CadastroForm()
            contexto = {"form": form}
            return render(request, 'form.html', contexto)
    else:
        # fluxo para exibir o formulário vazio GET
        contexto = {'form': form}
        return render(request, 'form.html', contexto)

def alunos_cadastrados(request):
    lista = CadastroModel.objects.all()
    alunos = {"alunos": lista}
    return render(request, 'alunos.html', alunos)
