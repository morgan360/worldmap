from allauth.account.forms import SignupForm, LoginForm
from django import forms
from users.models import Coupon, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from users.models import CustomUser
from django.core.exceptions import ValidationError

from allauth.account.forms import SignupForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class CouponSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'bg-pink-200 border-2 border-green-300 rounded py-2 px-4 block w-full',
            'placeholder': 'First name'
        }),
        required=True
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'bg-pink-200 border-2 border-gray-300 rounded py-2 px-4 block w-full',
            'placeholder': 'Last name'
        }),
        required=True
    )
    coupon_code = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'bg-pink-200 border-2 border-pink-300 rounded py-2 px-4 block w-full',
            'placeholder': 'Coupon code'
        }),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(CouponSignupForm, self).__init__(*args, **kwargs)
        # Updating all fields to use the same Tailwind CSS classes for consistency
        field_classes = 'bg-pink-200! border-2 border-pink-300 rounded py-2 px-4 block w-full'
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': field_classes
            })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email address'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Password (again)'
        })

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('email'),
            Field('first_name'),
            Field('last_name'),
            Field('password1'),
            Field('password2'),
            Field('coupon_code'),
            Submit('submit', 'Sign Up',
                   css_class='w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded')
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        # Update widget attributes to include Tailwind CSS classes
        self.fields['login'].widget.attrs.update(
            {'class': 'input bg-pink-300 border-2 border-pink-300 rounded py-2 px-4 block w-full',
             'placeholder': 'Your Email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'input bg-pink-300 border-2 border-pink-300 rounded py-2 px-4 block w-full',
             'placeholder': 'Password'})

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('email', css_class='text-blue-500'),  # Use Tailwind's text color utility class
            Field('password', css_class='text-blue-500'),
        )
        self.helper.form_show_labels = True