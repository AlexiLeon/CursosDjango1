from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

# ✅ Vista principal con formulario y tabla integrada
def cursos(request):
    cursos = Curso.objects.all()

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos')  # 👈 Redirige a sí misma para que veas los cursos
    else:
        form = CursoForm()

    return render(request, 'cursos/cursos.html', {'form': form, 'cursos': cursos})

# ✅ Vista alternativa SOLO para crear (opcional)
def crear_curso(request):
    cursos = Curso.objects.all()  # 👈 Se pasa la lista al template también

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crear_editar_curso')  # 👈 O cambiar por 'cursos' si prefieres redirigir a la tabla
    else:
        form = CursoForm()

    return render(request, 'cursos/crear_editar_curso.html', {'form': form, 'cursos': cursos})

# ✅ Vista auxiliar para mostrar cursos (solo tabla, si la usas)
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/crear_editar_cursos.html', {'cursos': cursos})




def eliminar_curso(request, id, confirmacion='cursos/confirmar_eliminacion.html'):
    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        curso.delete()
        cursos = Curso.objects.all()
        return render(request, 'cursos/crear_editar_curso.html', {'form': CursoForm(), 'cursos': cursos})

    return render(request, confirmacion, {'object': curso})



def consultar_curso_individual(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'cursos/form_editar_curso.html', {'curso': curso})



def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    form = CursoForm(request.POST, request.FILES, instance=curso)

    if form.is_valid():
        form.save()
        cursos = Curso.objects.all()
        return render(request, 'cursos/crear_editar_curso.html', {'form': CursoForm(), 'cursos': cursos})

    return render(request, 'cursos/form_editar_curso.html', {'curso': curso})


