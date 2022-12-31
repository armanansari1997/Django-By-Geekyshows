from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.

def addandshow(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = Student(name=name, email=email, password=password)
            reg.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stu = Student.objects.all()
    return render(request, 'enroll/home.html', {'form':fm, 'stu': stu})

def updatedata(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatedata.html', {'form':fm})


def deletedata(request, id):
    pi = Student.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

