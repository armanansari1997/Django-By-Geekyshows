from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    fm = StudentRegistration(initial='Arman Updated') # at runtime hence overriding prev
    return render(request, 'enroll/userregistration.html', {'form': fm})
