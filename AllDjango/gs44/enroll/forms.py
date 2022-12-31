from xml.dom import ValidationErr
from django.core import validators
from django import forms
        
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re-enter Password' ,widget=forms.PasswordInput)

    def clean(self):
        self.cleaned_data = super().clean()
        valpwd = self.cleaned_data['password']  # self.cleaned_data.get('password)
        valrpwd = self.cleaned_data['rpassword']

        if valpwd != valrpwd:
            raise forms.ValidationError('Password and Re-enter password is not matching')