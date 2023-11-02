from django import forms
from django.core.exceptions import ValidationError 

class tableForm(forms.Form):
    fila = forms.IntegerField(label='Fila:',max_value=20, required= True, initial=2)
    columna = forms.IntegerField(label='Columna',max_value=15, required= True, initial=2)
    minas = forms.IntegerField(label='Minas',max_value=150, required= True, initial=1)



    def clean(self):
        cleaned_data=super().clean()
        fila=cleaned_data.get("fila")
        columna=cleaned_data.get("columna")
        minas=cleaned_data.get("minas")

        if minas>((fila*columna)/2):
            raise ValidationError(
                "Ha introducido mas minas de las posibles"
                )
        
        return cleaned_data
    