from crispy_forms.helper import FormHelper
from django import forms

from core.colors import colors
from .models import Feedback
from crispy_forms.layout import Layout, Submit, Field

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']


# forms.py
from django import forms


class CustomContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Message',
    }), required=True)
    def __init__(self, *args, **kwargs):
        super(CustomContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'custom-font'
        self.helper.layout = Layout(
            Field('email', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full '),
                  )
