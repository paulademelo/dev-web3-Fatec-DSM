from django.shortcuts import render
from .models import CadastroModel
from .forms import CadastroForm


def index(request):
    return render(request, 'index.html')


def cadastro(request):
    
    data = {}
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            CadastroForm.objects.create(request.POST['name'],
                                            request.POST['curso'],
                                            request.POST['ano'],
                                            request.POST['semestre'],
                                            )
            return render(request, 'cadastro.html', data)
        else:
            # Fluxo sem gravar
            contexto = {'form': form}
            data['msg'] = "Erro ao cadastrar, tente novamente mais tarde"
            return render(request, 'index.html', data)
    else:
        # Fluxo para exibir o formulário vazio
        form = CadastroForm()
        contexto = {'form': form}
        data['msg'] = "Formulário vazio"
    return render(request, 'index.html')


def store(request):
    return render(request, 'cadastro.html')


def aluno(request):
    return render(request, 'aluno.html')
