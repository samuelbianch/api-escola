from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nome', 'nivel')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)
    list_per_page = 15


admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)
