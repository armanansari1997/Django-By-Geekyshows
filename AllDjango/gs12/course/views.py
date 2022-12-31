from django.shortcuts import render


# Create your views here.

def learn_django(request):
    coursename = {'cname': 'Django'}
    return render(request, 'course/courseone.html', context=coursename)  # here course is a folder
    # return render(request, 'course/courseone.html', coursename)
    # return render(request, 'course/courseone.html', {'cname': 'Laravel'})

def learn_python(request):
    cname = 'Python'
    duration = '3 months'
    seats = 10
    python_details = {'nm': cname, 'du': duration, 'st': seats}
    return render(request, 'course/coursetwo.html', python_details)
    # return render(request, 'course/coursetwo.html', context=python_details)