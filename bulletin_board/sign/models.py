from django.db import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUser(UserCreationForm):
    email = forms.EmailField(label='EMAIL',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Введите Email'}))
    username = forms.CharField(label='Ник',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Ник'}))
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'placeholder': 'Введите Имя'}))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Подтвердите пароль'}))



    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
