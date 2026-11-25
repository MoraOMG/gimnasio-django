from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class PlanEntrenamiento(models.Model):
    NIVELES = [
        ("principiante", "Principiante"),
        ("intermedio", "Intermedio"),
        ("avanzado", "Avanzado"),
    ]
    OBJETIVOS = [
        ("bajar_peso", "Bajar de peso"),
        ("masa_muscular", "Ganar masa muscular"),
        ("resistencia", "Resistencia"),
        ("flexibilidad", "Flexibilidad"),
    ]

    nombre = models.CharField("Nombre del plan", max_length=100, unique=True)
    objetivo = models.CharField("Objetivo", max_length=20, choices=OBJETIVOS)
    nivel = models.CharField("Nivel", max_length=15, choices=NIVELES)
    descripcion = models.TextField("Descripción")
    duracion_semanas = models.PositiveSmallIntegerField(
        "Duración (semanas)",
        validators=[MinValueValidator(1), MaxValueValidator(52)],
    )
    sesiones_por_semana = models.PositiveSmallIntegerField(
        "Sesiones por semana",
        validators=[MinValueValidator(1), MaxValueValidator(7)],
    )
    precio = models.DecimalField(
        "Precio (CLP)",
        max_digits=10,
        decimal_places=0,
        validators=[MinValueValidator(1)],
    )
    cupos = models.PositiveIntegerField("Cupos disponibles")
    entrenador_nombre = models.CharField("Entrenador a cargo", max_length=100)
    entrenador_email = models.EmailField("Correo del entrenador")
    activo = models.BooleanField("Plan activo", default=True)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        db_table = "plan_entrenamiento"
        ordering = ["-fecha_creacion"]
        verbose_name = "Plan de entrenamiento"
        verbose_name_plural = "Planes de entrenamiento"

    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_display()})"
