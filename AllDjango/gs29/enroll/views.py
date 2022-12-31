from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    # fm = StudentRegistration()
    # fm = StudentRegistration(auto_id='some_%s')  # some_[label_name]
    # fm = StudentRegistration(auto_id='geeky')  # It means True only [label_name]
    # fm = StudentRegistration(auto_id='False')
    # fm = StudentRegistration(auto_id='True')  # [label_name]

    # fm = StudentRegistration(auto_id='True', label_suffix=':') # default is colon(:) only
    # fm = StudentRegistration(auto_id='True', label_suffix='-')
    # fm = StudentRegistration(auto_id='True', label_suffix='A')
    # fm = StudentRegistration(auto_id='True', label_suffix=' ')

    fm = StudentRegistration(auto_id='True', label_suffix=' ', initial={'name':'Arman'})
    # fm = StudentRegistration(auto_id='True', label_suffix=' ', initial={'name':'Arman', 'email': 'arman@infobeans.com'})
    return render(request, 'enroll/userregistration.html', {'form': fm})
