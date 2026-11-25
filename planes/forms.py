from django import forms

from .models import PlanEntrenamiento


class BootstrapMixin:
    """Agrega clases de Bootstrap a todos los widgets."""

    def _aplicar_bootstrap(self):
        for campo in self.fields.values():
            widget = campo.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs["class"] = "form-check-input"
            elif isinstance(widget, forms.Select):
                widget.attrs["class"] = "form-select"
            else:
                widget.attrs["class"] = "form-control"


class ValidacionesPlanMixin:
    """Validaciones compartidas por el formulario de crear y el de editar."""

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data["descripcion"].strip()
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion

    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio

    def clean_cupos(self):
        cupos = self.cleaned_data["cupos"]
        if cupos < 0:
            raise forms.ValidationError("Los cupos no pueden ser negativos.")
        return cupos

    def clean_duracion_semanas(self):
        valor = self.cleaned_data["duracion_semanas"]
        if not 1 <= valor <= 52:
            raise forms.ValidationError("La duración debe estar entre 1 y 52 semanas.")
        return valor

    def clean_sesiones_por_semana(self):
        valor = self.cleaned_data["sesiones_por_semana"]
        if not 1 <= valor <= 7:
            raise forms.ValidationError("Las sesiones por semana deben estar entre 1 y 7.")
        return valor


CAMPOS_BASE = [
    "nombre",
    "objetivo",
    "nivel",
    "descripcion",
    "duracion_semanas",
    "sesiones_por_semana",
    "precio",
    "cupos",
    "entrenador_nombre",
    "entrenador_email",
]


class PlanCrearForm(BootstrapMixin, ValidacionesPlanMixin, forms.ModelForm):
    """Formulario para CREAR (no incluye 'activo': un plan nuevo nace activo)."""

    class Meta:
        model = PlanEntrenamiento
        fields = CAMPOS_BASE
        widgets = {"descripcion": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._aplicar_bootstrap()


class PlanEditarForm(BootstrapMixin, ValidacionesPlanMixin, forms.ModelForm):
    """Formulario para EDITAR (incluye 'activo' para poder desactivar el plan)."""

    class Meta:
        model = PlanEntrenamiento
        fields = CAMPOS_BASE + ["activo"]
        widgets = {"descripcion": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._aplicar_bootstrap()
