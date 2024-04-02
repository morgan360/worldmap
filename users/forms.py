from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core import colors
from users.models import Coupon, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from users.models import CustomUser
from django.core.exceptions import ValidationError
from crispy_forms.layout import Div


class CouponSignupForm(SignupForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'class': 'custom-font',
    }), required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last name'}),
        required=True
    )
    key_code = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Keycode'}),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(CouponSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'custom-font'
        self.helper.layout = Layout(
            Field('email', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full '),
            Field('first_name', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('last_name', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('password1', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('password2', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('key_code', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Div(Submit('submit', 'Sign Up', css_class=f'bg-[{colors.colors["button_color"]}] hover:bg-[{colors.colors["hover_button_color"]}] text-[{colors.colors["button_text_color"]}] font-bold py-2 px-4 rounded'), css_class='text-center'))
        self.helper.label_class = f'text-[{colors.colors["label_color"]}] font-normal text-lg'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'custom-font'
        self.helper.layout = Layout(
            Field('login', css_class='bg-green-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('password', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Div(Submit('submit', 'Sign In',
                       css_class=f'bg-[{colors.colors["button_color"]}] hover:bg-[{colors.colors["hover_button_color"]}]text-[{colors.colors["button_text_color"]}] font-bold py-2 px-4 rounded'),
                css_class='text-center')
        )
        self.helper.label_class = f'text-[{colors.colors["label_color"]}] font-normal text-lg'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']


