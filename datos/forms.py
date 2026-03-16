from django import forms

class CargarArchivoForm(forms.Form):
    archivo = forms.FileField()
