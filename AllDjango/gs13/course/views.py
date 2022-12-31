from django.shortcuts import render
from datetime import date, datetime

# Create your views here.

# def learn_django(request):
#     return render(request, 'course/courseone.html', context={'nm': 'Django'})

# def learn_django(request):
#     cname = 'Django'
#     duration = '4 Months'   
#     seats = 15
#     django_details = {'nm': cname, 'du': duration, 'st': seats}
#     return render(request, 'course/courseone.html', context=django_details)

# def learn_django(request):
#     return render(request, 'course/coursetwo.html', context={'nm': 'django is awesome'})

# def learn_django(request):
#     d = datetime.now()
#     return render(request, 'course/coursethree.html', context={'dt': d})

# def learn_django(request):
#     django_price = {'p1': 56.24321, 'p2': 56.00000, 'p3': 56.37000}
#     return render(request, 'course/coursefour.html', context=django_price)

# def learn_django(request):
#     # course_name = {'name': True}
#     # course_name = {'name': False}
#     # course_name = {'name': 'Django'}
#     using_operator_if = {'nm': 'Django', 'st': 5}
#     # return render(request, 'course/coursefive.html', context=course_name)
#     return render(request, 'course/coursefive.html', context=using_operator_if)

# def learn_django(request):
#     student = {'names': ['Rahul', 'Sonam', 'Anu', 'Raj']}
#     return render(request, 'course/coursesix.html', context=student)


# def learn_django(request):
#     stu = {'stu1': {'name': 'Rahul', 'roll': 101},
#             'stu2': {'name': 'Sonam', 'roll': 102},
#             'stu3': {'name': 'Raj', 'roll': 103},
#             'stu4': {'name': 'Anu', 'roll': 104},
#     }
#     students = {'student': stu}
#     return render(request, 'course/courseseven.html', context=students)

# def learn_django(request):
#     data = {'name': 'Rahul', 'roll': 101}
#     return render(request, 'course/courseeight.html', context={'dt': data})

def learn_django(request):
    data = {'stu1': {'name': 'Rahul', 'roll': 101},
            'stu2': {'name': 'Sonam', 'roll': 102},
            'stu3': {'name': 'Raj', 'roll': 103},
            'stu4': {'name': 'Anu', 'roll': 104},
    }
    return render(request, 'course/coursenine.html', context={'dt': data})
    