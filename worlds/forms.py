from django import forms
from .models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['id', 'name', 'description', 'supertype', 'subtype',  'image_url']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'supertype': forms.TextInput(attrs={'class': 'form-control'}),
            'subtype': forms.TextInput(attrs={'class': 'form-control'}),
            # 'creation_time_stamp': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_url': forms.Textarea(attrs={'class': 'form-control'}),
        }
