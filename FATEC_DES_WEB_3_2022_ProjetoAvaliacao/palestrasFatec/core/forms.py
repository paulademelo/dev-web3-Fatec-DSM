from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=50)
    curso = forms.CharField(max_length=50)
    ano = forms.CharField(max_length=50)
    semestre = forms.CharField(max_length=50)
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()