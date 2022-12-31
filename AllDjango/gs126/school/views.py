from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import ContactForm, FeedbackForm

# Create your views here.

class ContactFormView(FormView):
    template_name = 'school/contact.html'

    form_class = ContactForm
    # form_class = FeedbackForm

    initial = {'name': 'Arman'}
    success_url = '/thankyou/'

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
        # return HttpResponse('Msg Sent')

class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'

