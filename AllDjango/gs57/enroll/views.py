from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistration

# Create your views here.

def regi(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'User has been created successfully !!!')

            # recommended way to send messages 
            messages.info(request, 'Now you can login')

    else:
        fm = UserRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})