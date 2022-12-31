from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

        # All attributes
        labels = {'name': 'Enter Name', 'password': 'Enter your password', 'email': 'Enter Email'}
        
        # !important for passwordInput
        widgets = {'password': forms.PasswordInput,} 

