from django.shortcuts import render
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})
