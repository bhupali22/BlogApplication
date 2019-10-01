from django.utils.deprecation import MiddlewareMixin


# class BlogMiddleware:
#     def __init__(self, get_response):
#         # One-time configuration and initialization.
#         self.get_response = get_response
#         print("In the init")
#
#     def __call__(self,request, *args, **kwargs):
#         # Code to be executed for each request before the view (and later middleware) are called.
#
#         print("In the call")
#         self.process_request()
#         return self.get_response(request)
#
#     def process_request(self, request):
#         print("In process_request")


class BlogMiddleware(MiddlewareMixin):          #when we use MiddlewareMixin then we dont need to write __init__ and __call__. Also if we defined process_request or response then they are called automatically.
    def process_request(self, request):
        print("In process request")


    def process_response(self,request, response):       #it must return an HttpResponse otherwise it will give error "AttributeError: 'NoneType' object has no attribute '_closable_objects'" : NoneType means that instead of an instance of whatever Class or Object you think you're working with, you've actually got None. That usually means that an assignment or function call up above failed or returned an unexpected result.
        print("In process_response")
        return response

    def process_view(self, request,search_blog ,*args, **kwargs):
        print("In process_view")




