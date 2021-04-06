from django.http import HttpResponse


# Create your views here.
def hello(request, resource=None):

    html = f"<h1>Hello {resource or 'World'}</h1>"
    return HttpResponse(html)