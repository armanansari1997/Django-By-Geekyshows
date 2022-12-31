from http.client import ImproperConnectionState
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(initial='Arman', help_text='is field me 30 char hi likh sakte hai')