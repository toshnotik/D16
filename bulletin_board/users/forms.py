from allauth.account.forms import LoginForm, SignupForm, BaseSignupForm
from django import forms
from django.forms import CharField, TextInput, PasswordInput, EmailField


class MyLoginForm(LoginForm):
    # услевие для применения ACCOUNT_FORMS в settings
    """Переопределить форму вхожа allauth"""
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'] = CharField(
            label=("E-MAIL"), widget=TextInput(attrs={'class': 'form-control', }))
        self.fields['password'].widget = PasswordInput(
            attrs={'class': 'form-control', })


class MySignupForm(SignupForm):
    # можно по разному переопределять форму. Так:
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "type": "email",
                "placeholder": "E-mail address",
                "autocomplete": "email",
            }
        )
    )