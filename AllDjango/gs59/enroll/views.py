from email import message
from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistration

# Create your views here.

def regi(request):
    messages.info(request, 'Now you can Login')
    messages.success(request, 'Updated Successfully')
    messages.warning(request, 'This is a warning')
    messages.error(request, 'This is an error')
    fm = UserRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})