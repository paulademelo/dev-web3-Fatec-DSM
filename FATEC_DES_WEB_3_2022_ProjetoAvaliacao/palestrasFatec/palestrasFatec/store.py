from django.shortcuts import render
from django.contrib.auth.models import User

# Formulário de cadastro de usuários


def create(request):
    return render(request, 'cadastro.html')

# Inserção dos dados dos usuários no banco


def store(request):
    data = {}
    user = User.objects.create_user(
        request.POST['name'], request.POST['curso'], request.POST['ano'], request.POST['semestre'])
    user.first_name = request.POST['name']
    user.save()
    data['msg'] = 'Aluno cadastrado com sucesso!'
    data['class'] = 'alert-success'
    return render(request, 'cadastro.html', data)
