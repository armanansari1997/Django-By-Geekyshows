from django.shortcuts import HttpResponse, render

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("I am Under Construction before View")
        # response = HttpResponse("This site is Under Construction")
        response = render(request, 'mysite/siteuc.html')
        print("I am Under Construction after View")
        return response