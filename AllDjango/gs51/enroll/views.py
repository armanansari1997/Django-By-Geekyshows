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

            # insert/save the data to table
            reg = User(name=nm, email=em, password=pwd)
            reg.save()

            # update the data of table using id field
            # reg = User(id=3, name=nm, email=em, password=pwd)
            # reg.save()

            # delete the data of table using id field
            # reg = User(id=2)
            # reg.save()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})
