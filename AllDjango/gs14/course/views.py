from django.shortcuts import render

# Create your views here.

def learn_django(request):
    return render(request, 'course/info.html', context={'nm': 'Django Course'})