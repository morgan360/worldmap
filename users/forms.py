from allauth.account.forms import SignupForm
from django import forms
from users.models import Coupon, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from users.models import CustomUser
from django.core.exceptions import ValidationError


class CouponSignupForm(SignupForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'}),
        required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'}),
        required=True
    )
    coupon_code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'}),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(CouponSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('email', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('first_name', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('last_name', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('password1', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('password2', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Field('coupon_code', css_class='bg-gray-200 border-2 border-gray-300 rounded py-2 px-4 block w-full'),
            Submit('submit', 'Sign Up', css_class='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded')
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
