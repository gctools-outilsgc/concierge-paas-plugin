from .models import Configuration
from django import forms
from django.forms import ModelForm, PasswordInput

class AdminForm(ModelForm):
    password = forms.CharField(widget=PasswordInput())
    class Meta:
        model = Configuration