from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Count, Min, Max, Sum

# Create your views here.

def home(request):

    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    total = student_data.aggregate(Sum('marks'))
    totalcount = student_data.aggregate(Count('marks'))
    print(average)

    context = {'students': student_data, 'average': average, 'minimum': minimum, 'maximum':maximum, 'total':total, 'totalcount':totalcount}

    print('Return :', student_data)
    print()
    print('SQL Query :', student_data.query)
    return render(request, 'school/home.html', context)
