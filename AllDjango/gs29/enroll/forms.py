from http.client import ImproperConnectionState
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()  # Name
    email = forms.EmailField()  # Email
    first_name = forms.CharField  # First name