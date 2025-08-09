from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('', views.lista_cursos, name='cursos'),
    path('crear/', views.crear_curso, name='crear_editar_curso'),
    path('eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
    path('editar_curso/<int:id>/', views.editar_curso, name='editar_curso'),
    path('form_editar_curso/<int:id>/', views.consultar_curso_individual, name='consulta_curso'),
]
