from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Customer, ProjectName, FinalProductNumber, SingleProductsNumber


class Login(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput)