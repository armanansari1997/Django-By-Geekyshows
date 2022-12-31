from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from .models import Post

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", label_suffix="", widget=forms.PasswordInput(attrs={'class': 'form-control my-2'}))
    password2 = forms.CharField(label="Confirm Password", label_suffix="", widget=forms.PasswordInput(attrs={'class': 'form-control my-2'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control my-2'}),
            'first_name': forms.TextInput(attrs={'class':'form-control my-2'}),
            'last_name': forms.TextInput(attrs={'class':'form-control my-2'}),
            'email': forms.EmailInput(attrs={'class':'form-control my-2'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(label_suffix="", widget=forms.TextInput(attrs={
            'autofocus': True, 'class': 'form-control my-2', 'placeHolder': 'Enter your username'
        }))
    password = forms.CharField(label_suffix="", label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={ 'autocomplete': True, 'class': 'form-control my-2', 'placeHolder': 'Enter your password'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        labels = {'title':'Title', 'desc': 'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }