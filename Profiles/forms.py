from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(ModelForm):
    class Meta:
        model=User
        fields=('username',)