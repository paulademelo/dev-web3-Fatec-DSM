from django.db import models

# a classe models é onde ficará os atributos do banco de dados

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado', max_length=50)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mes')
    modificado_em = models.DateTimeField(verbose_name='modificado em', auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.nome + '=> ' + str(self.dia)

        
    '''
    para criar arquivo de migração do django, usar:
    python manage.py makemigrations

    para fazer a migração:
    python manage.py migrations
    '''
