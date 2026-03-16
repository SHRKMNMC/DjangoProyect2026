from django import forms

class MensajeForm(forms.Form):
    contenido = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 2,
            "placeholder": "Escribe un mensaje..."
        })
    )
