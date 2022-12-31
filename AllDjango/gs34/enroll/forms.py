from http.client import ImproperConnectionState
from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField(label='Your Name')
    # name = forms.CharField(label='Your Name', label_suffix=' ')
    # name = forms.CharField(label='Your Name', label_suffix=' ', initial='Arman')
    # name = forms.CharField(label='Your Name', label_suffix=' ', initial='Arman', required=False) # default value of required=True
    # name = forms.CharField(label='Your Name', label_suffix=' ', initial='Arman', required=False, disabled=True)
    # name = forms.CharField(label='Your Name', label_suffix=' ', initial='Arman', required=False, disabled=True)
    name = forms.CharField(label='Your Name', label_suffix=' ', initial='Arman', required=False, disabled=True, help_text='Limit 70 char')