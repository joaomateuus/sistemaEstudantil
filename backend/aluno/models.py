from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'