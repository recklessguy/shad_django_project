from django import forms
from django.forms import widgets
from .models import new_ghazals


class newghazalform(forms.ModelForm):
    class Meta:
        model = new_ghazals
        fields = ['name', 'tags', 'writer', 'shayari']

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'tags':forms.TextInput(attrs={'class': 'form-control'}),
            'writer':forms.TextInput(attrs={'class': 'form-control'}),
            'shayari':forms.Textarea(attrs={'class': 'form-control'}),
        }