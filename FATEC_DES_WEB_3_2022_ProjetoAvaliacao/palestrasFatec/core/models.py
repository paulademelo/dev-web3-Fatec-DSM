from django.db import models


class CadastroModel(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    ano = models.CharField(max_length=50)
    semestre = models.CharField(max_length=50)

    def __str__(self):
        return self.nome + '=> ' + str(self.dia)
    
    class Meta:
        verbose_name = 'Palestras'
        verbose_name_plural = 'Palestras'