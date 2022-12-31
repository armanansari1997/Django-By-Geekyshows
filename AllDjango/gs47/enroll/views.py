from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']

            # register/insert the data into the User table columns
            reg = User(name=nm, email=em, password=pwd)
            reg.save()

            # Update the data of table(use id)
            # reg = User(id = 5, name=nm, email=em, password=pwd)
            # reg.save()

            # Delete the data from the table
            # reg = User(id=4)
            # reg.delete()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})
