from django import forms
from django.forms import ModelForm

from .models import Coordinates


class CoordinatesForm(forms.ModelForm):
    latitude = forms.CharField(max_length=20)  # Use forms.CharField instead of models.CharField
    longitude = forms.CharField(max_length=20)  # Use forms.CharField instead of models.CharField

    class Meta:
        model = Coordinates
        fields = '__all__'


class DeleteCoordinatesForm(forms.Form):
    coordinates_to_delete = forms.ModelMultipleChoiceField(queryset=Coordinates.objects.all(),
                                                           widget=forms.CheckboxSelectMultiple)
