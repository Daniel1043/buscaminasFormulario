from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
     path("Tablas", views.form_tablero, name="crear_tablero"),
]
