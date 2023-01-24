from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):

    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    nome = models.CharField(max_length=100)
    codigo = models.IntegerField()
    nivel = models.CharField(max_length=1, blank=False, null=False, choices=NIVEL, default='B')

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, blank=False, null=False, choices=PERIODO, default='M')