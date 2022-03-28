from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def if_user_exists(login):
    if get_user_model().objects.filter(username=login).exists():
        raise ValidationError('Taki użytkownik już istnieje')


class RegisterUserForm(forms.Form):
    login = forms.CharField(validators=[if_user_exists])
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password != repeat_password:
            raise forms.ValidationError("Passwords don't match")


class LoginForm(forms.Form):
    login = forms.CharField(label='login', max_length=120)
    password = forms.CharField(label='password', max_length=120, widget=forms.PasswordInput)