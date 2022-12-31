from django.shortcuts import render

# Create your views here.

def learn_django(request):
    title = 'Learn Django'
    cname = 'Django'
    dejango_details = {'title': title, 'cname': cname}
    return render(request, 'course/courseone.html', context=dejango_details)