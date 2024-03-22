from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']


# forms.py
from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Your message'}))
