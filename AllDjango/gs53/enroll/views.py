from django.shortcuts import render

# Create your views here.

def home(request, check):
    return render(request, 'enroll/home.html', context={'ch': check})

# def show_details(request, my_id):
#     student = {'id': my_id}
#     return render(request, 'enroll/show.html', student)

def show_details(request, my_id=1):
    if my_id == 1:
        student = {'id': my_id, 'name': 'Arman'}
    if my_id == 2:
        student = {'id': my_id, 'name': 'Madhur'}
    if my_id == 3:
        student = {'id': my_id, 'name': 'Rusia'}
    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id, my_subid):
    if my_id == 1 and my_subid == 4:
        student = {'id': my_id, 'name': 'Arman', 'info': 'Sub Details'}
    if my_id == 2 and my_subid == 6:
        student = {'id': my_id, 'name': 'Madhur', 'info': 'Sub Details'}
    if my_id == 3 and my_subid == 7:
        student = {'id': my_id, 'name': 'Rusia', 'info': 'Sub Details'}
    return render(request, 'enroll/show.html', student)

