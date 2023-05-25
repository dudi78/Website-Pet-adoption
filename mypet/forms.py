from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class RegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=20)

    class Meta:
        model = MyUser
        fields = ['username', 'password1', 'password2', 'email', 'phone']
