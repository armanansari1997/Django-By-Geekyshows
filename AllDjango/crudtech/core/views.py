from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Student
from .forms import AddStudentForm
# Create your views here.

class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html', {'studata': stu_data})


class AddStudent(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'core/addstudent.html', {'form': fm})
    
    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            roll = fm.cleaned_data['roll']
            city = fm.cleaned_data['city']
            user = Student(name=name, roll=roll, city=city)
            user.save()
            return redirect('/')
        else:
            return render(request, 'core/addstudent.html', {'form': fm})

class DeleteStudent(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        Student.objects.get(id=id).delete()
        return redirect('/')

class EditStudent(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'core/updatestudent.html', {'form': fm})
    
    def post(self,request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')