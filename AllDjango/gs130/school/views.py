from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from .forms import StudentForm
from .models import Student
from django import forms

# Create your views here.

# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/thanks/'

#     def get_form(self):
#         form = super().get_form()
#         form.fields.get('name').widget = forms.TextInput(attrs={ 'class': 'myclass'})
#         form.fields.get('password').widget = forms.PasswordInput(attrs={ 'class': 'mypass'})
#         return form

class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'


# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/thanksupdate/'

#     def get_form(self):
#         form = super().get_form()
#         form.fields.get('name').widget = forms.TextInput(attrs={ 'class': 'myclass'})
#         form.fields.get('password').widget = forms.PasswordInput(attrs={ 'class': 'mypass'})
#         return form


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate/'


class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanksupdate.html'





