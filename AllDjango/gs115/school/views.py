from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.

def homefun(request):
    return render(request, 'school/home.html')

class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html') 


########################################################################################

def aboutfun(request):
    context = {'msg':' Welcome to GeekyShows Function Based View'}
    return render(request, 'school/about.html', context)

class AboutClassView(View):
    def get(self, request):
        context = {'msg':' Welcome to GeekyShows Function Based View'}
        return render(request, 'school/about.html', context)


########################################################################################

def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You for Form Submition !!!')
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form':form})
    

class CotactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form':form})
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            # print(request.POST['name'])
            return HttpResponse('Thank You for Form Submition !!!')


###########################################################################################

# def newsfun(request):
#     template_name = 'school/news.html'
#     context = {'info':'CBI enquiry Why GeekyShows earns less money'}
#     return render(request, template_name, context)

def newsfun(request, template_name):
    context = {'info':'CBI enquiry Why GeekyShows earns less money'}
    return render(request, template_name, context)


# class NewsClassView(View):
#     template_name = 'school/news.html'
#     def get(self, request):
#         context = {'info':'CBI enquiry Why GeekyShows earns less money'}
#         return render(request, self.template_name, context)

class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info':'CBI enquiry Why GeekyShows earns less money'}
        return render(request, self.template_name, context)
        
        