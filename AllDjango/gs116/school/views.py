from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

# class HomeTemplateView(TemplateView):
#     template_name = 'school/home.html'


# Using Context
class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'Sonam' 
        context["roll"] = 101 

        # or (using this extra_context won't work)
        # context = {'name': 'Arman', 'roll': 101}
        print(context)
        print(kwargs)
        return context
    

