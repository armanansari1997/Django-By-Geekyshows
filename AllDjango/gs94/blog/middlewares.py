from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    # Hook - 1
    def process_view(self, request, *args, **kwargs):
        print("This is Process View - Before view")
        # return HttpResponse("This is before view")
        return None


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    # Hook - 2
    def process_exception(self, request, exception):
        print("Exception Occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    # Hook - 3
    def process_template_response(self, request, response):
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'Sonam'
        return response