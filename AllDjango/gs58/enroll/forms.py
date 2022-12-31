from django import forms
from .models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'email']
