from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    fm = StudentRegistration()
    # fm.order_fields(field_order=None)  # this is default
    fm.order_fields(field_order=['first_name', 'name', 'email'])
    return render(request, 'enroll/userregistration.html', {'form': fm})
