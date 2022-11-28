from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CadastroModel
from .forms import CadastroForm


def index(request):
    return render(request, 'index.html')


def cadastro(request):
    data = {}
    if request.method == 'POST':

        form = CadastroForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['nome'],
                                       request.POST['curso'],
                                       request.POST['ano'],
                                       request.POST['semestre'],
                                       )
            # Fluxo para gravar
            user.save()
            return render(request, 'cadastro.html', contexto)
        else:
            # Fluxo sem gravar
            contexto = {'form': form}
            data['msg'] = "Erro ao cadastrar, tente novamente mais tarde"
            return render(request, 'cadastro.html', contexto)
    else:
        # Fluxo para exibir o formulário vazio
        form = CadastroForm()
        contexto = {'form': form}
        data['msg'] = "Formulário vazio"
        return render(request, 'cadastro.html', contexto)


def store(request):
    return render(request, 'store.html')


def aluno(request):
    return render(request, 'aluno.html')
