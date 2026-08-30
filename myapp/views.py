
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello from MyApp Home Page!")


def about(request):
    return HttpResponse("This is the About Page.")