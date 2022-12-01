from django import forms

# refatorar para o core
class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=20)
    curso = forms.CharField(max_length=50)
    semestre = forms.IntegerField()
    ano = forms.IntegerField()
