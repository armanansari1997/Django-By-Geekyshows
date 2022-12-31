from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'Arman'
    request.session['lname'] = 'Ansari'
    return render(request, 'student/setsession.html')



def getsession(request):
    name = request.session.get('name', 'Guest')
    keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', 25)
    # return render(request, 'student/getsession.html', {'name': name, 'keys': keys, 'items': items, 'age': age})
    return render(request, 'student/getsession.html', {'name': name, 'keys': keys, 'items': items})



def delsession(request):
    request.session.flush()
    return render(request, 'student/delsession.html')