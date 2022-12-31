from http.client import ImproperConnectionState
from xml.dom import ValidationErr
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)

    def clean(self):
        self.cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 4:
            raise forms.ValidationError('Name should be more than or equal to 4')
        if len(valemail) < 10:
            raise ValidationErr('Email Should be more than or equal to 10')