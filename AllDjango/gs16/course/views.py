from django.shortcuts import render

# Create your views here.

def learn_django(request):
    django_details = {'title': 'Django', 'cname': 'Django'}
    return render(request, 'course/courseone.html', context=django_details)
