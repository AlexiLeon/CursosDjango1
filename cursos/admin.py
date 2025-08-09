from django.contrib import admin

from django.contrib import admin
from .models import Curso
from .models import Actividad

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre', 'nivel', 'duracion_horas', 'costo', 'creado_en')
    search_fields = ('clave', 'nombre', 'descripcion')
    list_filter = ('nivel', 'creado_en')
    date_hierarchy = 'creado_en'
    ordering = ('creado_en',)
    fieldsets = (
        ('Información General', {
            'fields': ('clave', 'nombre', 'descripcion')
        }),
        ('Detalles del Curso', {
            'fields': ('nivel', 'duracion_horas', 'costo')
        }),
        ('Imagen y Fecha', {
            'fields': ('imagen', 'creado_en')
        }),
    )
    readonly_fields = ('creado_en',)

    

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('clave', 'curso', 'fecha_creacion')
    search_fields = ('clave', 'curso__nombre')
    list_filter = ('curso',)
    date_hierarchy = 'fecha_creacion'
    readonly_fields = ('fecha_creacion',)



# Cambiar nombre de la app en el panel
admin.site.site_header = 'CONVOCATORIAS'
admin.site.index_title = 'Cursos'
admin.site.register(Actividad, ActividadAdmin)
