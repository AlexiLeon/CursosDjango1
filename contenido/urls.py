from django.urls import path
from . import views

# Definimos las rutas de la app contenido
urlpatterns = [
    path('', views.pagina_principal, name='PaginaPrincipal'),  # Página de inicio
    path('cursos/', views.cursos, name='cursos'),  # Página de cursos
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
]
