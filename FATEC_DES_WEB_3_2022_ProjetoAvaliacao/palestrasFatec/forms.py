from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=20)
    sobrenome = forms.CharField(max_length=50)
    curso = forms.CharField(max_length=50)
    semestre = forms.IntegerField()
    ano = forms.IntegerField()
  
    def clean_nome(self):
        nome = self.clean_nome[nome]
        return nome.upper  