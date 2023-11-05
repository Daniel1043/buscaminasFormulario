from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import tableForm
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'tablas/index.html')

def form_tablero(request):
    if request.method == 'POST':
        table_form = tableForm(request.POST)
        table_form_v = tableForm()

        if table_form.is_valid():
            columna = int(table_form.cleaned_data['columna'])
            fila = int(table_form.cleaned_data['fila'])
            minas = int(table_form.cleaned_data['minas'])

            filas_list = range(fila)
            columnas_list = range(columna)
            minas_list = range(minas)

            return render(request, 'tablas/Tablas.html', {'columna': columnas_list, 'fila': filas_list, 'table_form': table_form_v})

    else:
        table_form = tableForm()

    return render(request, 'tablas/Tablas.html', {'table_form': table_form})
