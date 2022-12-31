from distutils.log import error
from xml.dom import ValidationErr
from django import forms
        
class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter Your Name'})
    email = forms.EmailField(min_length= 5, max_length= 40, error_messages={'required': 'Enter Your Email'})
    password = forms.CharField(min_length= 5, max_length= 40, widget=forms.PasswordInput, error_messages={'required': 'Enter Your Password'})