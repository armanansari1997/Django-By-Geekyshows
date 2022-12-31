from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

# Function Based View
def func(request):
    return HttpResponse('<h1>Function Based View</h1>')

# class Based View
class MyView(View):
    name = 'sonam'
    def get(self,request):
        # return HttpResponse('<h1>Class Based View - GET</h1>')
        return HttpResponse(f'<h1>{self.name}</h1>')

class MyChildView(MyView):
    def get(self,request):
        return HttpResponse(f'<h1>{self.name}</h1>')