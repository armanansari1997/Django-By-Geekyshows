from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def show_data(request):
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})
