from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.

def home(request):
    # Select all data
    # student_data = Student.objects.all()

    # Select data whose marks is equal to 70
    # student_data = Student.objects.filter(marks=70)

    # Select data whose marks is not equal to 70
    # student_data = Student.objects.exclude(marks=70)

    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('-marks')
    # student_data = Student.objects.order_by('?')
    # student_data = Student.objects.order_by('name')

    # student_data = Student.objects.order_by('id').reverse()

    # Limit 5 in Asc Order
    # student_data = Student.objects.order_by('id')[0:5]
    # Limit 5 in Desc Order
    # student_data = Student.objects.order_by('id').reverse()[:5]
    # student_data = Student.objects.order_by('-id')[0:5]

    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name', 'city')

    # student_data = Student.objects.values_list('id', 'name', named=True)

    # student_data = Student.objects.using('default')

    # student_data = Student.objects.dates('pass_date', 'month')
    # student_data = Student.objects.dates('pass_date', 'year')

############### Second tables 'Teacher' started   #################################

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1, all=True)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.intersection(qs1)
    # (or)
    # student_data = qs1.intersection(qs2)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs1.difference(qs2)
    # (or)
    # student_data = qs2.difference(qs1)

###################  AND OR Operator  ############################
    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6, roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))


    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=107)
    student_data = Student.objects.filter(Q(id=6) | Q(roll=107))


    print('Return :', student_data)
    print()
    print('SQL Query :', student_data.query)
    return render(request, 'school/home.html', {'students': student_data})


