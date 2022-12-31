from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistration

# Create your views here.

def regi(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Now you can login')
            print(messages.get_level(request))
            messages.debug(request, 'This is Debug')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'This is New Debug')
            print(messages.get_level(request))
    else:
        fm = UserRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})