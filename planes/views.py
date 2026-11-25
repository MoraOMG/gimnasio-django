from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PlanCrearForm, PlanEditarForm
from .models import PlanEntrenamiento


def inicio(request):
    contexto = {
        "total": PlanEntrenamiento.objects.count(),
        "activos": PlanEntrenamiento.objects.filter(activo=True).count(),
        "ultimos": PlanEntrenamiento.objects.all()[:3],
    }
    return render(request, "planes/inicio.html", contexto)


# R - Consultar
def plan_lista(request):
    planes = PlanEntrenamiento.objects.all()
    q = request.GET.get("q", "").strip()
    nivel = request.GET.get("nivel", "")
    if q:
        planes = planes.filter(Q(nombre__icontains=q) | Q(entrenador_nombre__icontains=q))
    if nivel:
        planes = planes.filter(nivel=nivel)
    contexto = {
        "planes": planes,
        "q": q,
        "nivel": nivel,
        "niveles": PlanEntrenamiento.NIVELES,
    }
    return render(request, "planes/plan_lista.html", contexto)


# C - Crear
def plan_crear(request):
    if request.method == "POST":
        form = PlanCrearForm(request.POST)
        if form.is_valid():
            plan = form.save()
            messages.success(request, f"El plan «{plan.nombre}» fue creado correctamente.")
            return redirect("planes:lista")
    else:
        form = PlanCrearForm()
    return render(request, "planes/plan_crear.html", {"form": form})


# U - Modificar
def plan_editar(request, pk):
    plan = get_object_or_404(PlanEntrenamiento, pk=pk)
    if request.method == "POST":
        form = PlanEditarForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, f"El plan «{plan.nombre}» fue actualizado.")
            return redirect("planes:lista")
    else:
        form = PlanEditarForm(instance=plan)
    return render(request, "planes/plan_editar.html", {"form": form, "plan": plan})


# D - Eliminar (con página de confirmación)
def plan_eliminar(request, pk):
    plan = get_object_or_404(PlanEntrenamiento, pk=pk)
    if request.method == "POST":
        nombre = plan.nombre
        plan.delete()
        messages.success(request, f"El plan «{nombre}» fue eliminado.")
        return redirect("planes:lista")
    return render(request, "planes/plan_eliminar.html", {"plan": plan})
