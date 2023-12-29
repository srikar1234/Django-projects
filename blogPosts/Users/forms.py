from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegisterForm(UserCreationForm):
    #default is required = true
    email = forms.EmailField()
    #Gives us a nested name space for configurations and keeps the config in one place
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']