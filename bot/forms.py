from django import forms
from .models import MensajeBot

class BotForm(forms.ModelForm):
    class Meta:
        model = MensajeBot
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe algo...'})
        }
