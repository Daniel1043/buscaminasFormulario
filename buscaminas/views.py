from django.shortcuts import render, redirect
from .forms import tableForm
from .minas_bomba import  Casilla, Tablero

def index(request):
    return render(request, 'tablas/index.html')

def form_tablero(request):
    tablero = None
    if request.method == 'POST':
        form = tableForm(request.POST)

        if form.is_valid():
            filas = form.cleaned_data['fila']
            columnas = form.cleaned_data['columna']
            num_minas = form.cleaned_data['minas']
                # Crea una instancia de Tablero y genera el tablero con minas
            tablero = Tablero(filas, columnas, num_minas).mostrar_tablero()
    else:
        form = tableForm()
    if tablero is not None:
        return render(request, 'tablas/Tablas.html', {'form': form, 'tablero': tablero})
    else:
        return render(request, 'tablas/crear_tabla.html', {'form': form})

