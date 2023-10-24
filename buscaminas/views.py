from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import tableForm
from django.shortcuts import render, get_object_or_404

def index(req):
   return render(req, 'tablas/index.html')


def form_tablero(request):
    if request.method == 'GET':
        table_form = tableForm(request.GET)
        table_form_v = tableForm()
        if table_form.is_valid():
           
            columna = int(table_form.cleaned_data['columna'])
            fila = int(table_form.cleaned_data['fila'])

            filas_list = range(fila)
            columnas_list = range(columna)
            
            return render(request, 'tablas/Tablas.html', {'columna': columnas_list , "fila": filas_list , "table_form":table_form_v})
    else:
        table_form = tableForm()

    return render(request, 'tablas/Tablas.html', {'table_form': table_form})
# Create your views here.
