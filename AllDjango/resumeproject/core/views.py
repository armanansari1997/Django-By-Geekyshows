from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html', context={'title': 'Home', 'home': 'active'})

def contact(request):
    return render(request, 'core/contact.html', context={'title': 'Contact', 'contact': 'active'})