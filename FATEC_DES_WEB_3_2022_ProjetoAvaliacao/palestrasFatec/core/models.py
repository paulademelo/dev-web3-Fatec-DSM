from django.db import models

class CadastroModel(models.Model):
    nome = models.CharField(max_length=20)
    curso = models.CharField(max_length=50)
    semestre = models.IntegerField()
    ano = models.IntegerField()

    def __str__(self):
        return self.nome  