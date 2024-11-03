from django.contrib.auth.forms import UserCreationForm, ValidationError
from django import forms
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=30, label='Select username')
    email = forms.EmailField(required=True, label='Email address')
    first_name = forms.CharField(required=True, max_length=50, label='First name')
    last_name = forms.CharField(required=True, max_length=50, label='Last name')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', ]


    def clean(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if User.objects.filter(username=cleaned_data["username"]).exists():
            raise ValidationError("This username is taken, please try another one")

        elif password1 != password2:
            raise ValidationError("2 password fields do not match")

        elif len(password1) < 8 or len(password2) < 8:
            raise ValidationError("Passwords must be at least 8 characters long")


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=30, label='Enter username')
    password = forms.CharField(required=True, label='Enter password', widget= forms.PasswordInput)