from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# Create your views here.

class StudentListView(ListView):
    model = Student

    # Auto Creating these 3 lines by using 1 line above code
    # stud = Student.objects.all()
    # context = {'student_list': stud}
    # return render(request, 'school/student_list.html', context)