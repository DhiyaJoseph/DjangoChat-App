from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # Your form fields and customization go here
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
