from django.shortcuts import render

# Vista para la página de inicio
def pagina_principal(request):
    return render(request, 'PaginaPrincipal.html')


# Vista para la página de cursos, con lista de cursos disponibles
def cursos(request):
    return render(request, 'cursos.html')


# Vista para la página de contacto
def contacto(request):
    return render(request, 'contacto.html')
