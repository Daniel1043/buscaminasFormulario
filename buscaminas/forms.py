from django import forms

class tableForm(forms.Form):
    fila = forms.CharField(label='Fila:',max_length=20)
    columna = forms.CharField(label='Columna',max_length=15)