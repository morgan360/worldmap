from django import forms
from .models import Feedback
from allauth.account.forms import LoginForm as AllauthLoginForm


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']


# forms.py
from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Your message'}))





class CustomLoginForm(AllauthLoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            if fieldname == 'remember':
                # Only apply specific classes to the checkbox, remove 'w-full'
                field.widget.attrs.update({
                    'class': 'form-checkbox h-5 w-5 text-blue-600'
                })
            else:
                # For other fields, keep 'w-full' and other classes
                field.widget.attrs.update({
                    'class': 'w-full bg-gray-600 text-white rounded border border-gray-600 p-3 leading-tight'
                })