from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


        # All attributes
        labels = {'name': 'Enter Name', 'password': 'Enter your password', 'email': 'Enter Email'}
        error_messages = {
            'name': {'required': 'Naam likhna zaruri hai'},
            'password': {'required': 'Password likhna zaruri hai'},
            }
        
        # !important for passwordInput
        widgets = {
            'password': forms.PasswordInput,
            'name': forms.TextInput(attrs={'class': 'myclass',
            'placeholder': 'Yaha Naam Likhiye'})
            } 

