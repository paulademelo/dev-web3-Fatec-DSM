from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=20)
    curso = forms.CharField(max_length=50)
    semestre = forms.IntegerField()
    ano = forms.IntegerField()
