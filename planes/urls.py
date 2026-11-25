from django.urls import path

from . import views

app_name = "planes"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("planes/", views.plan_lista, name="lista"),
    path("planes/nuevo/", views.plan_crear, name="crear"),
    path("planes/<int:pk>/editar/", views.plan_editar, name="editar"),
    path("planes/<int:pk>/eliminar/", views.plan_eliminar, name="eliminar"),
]
