from django.shortcuts import render

# Create your views here.

def fees_django(request):
    django_details = {'title': 'Django Fees', 'cname': 'Django', 'charge': 500}
    return render(request, 'fees/feesone.html', context=django_details)
