from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label=_("User"), max_length=50, required=True)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
