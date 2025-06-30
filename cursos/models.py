from django.db import models

from django.db import models

class Curso(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=50, choices=[
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ])
    duracion_horas = models.IntegerField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    creado_en = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.clave})"

    class Meta:
        ordering = ['creado_en']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
