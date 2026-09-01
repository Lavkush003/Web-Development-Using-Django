
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello from MyApp Home Page!")


def about(request):
    return HttpResponse("This is the About Page.")



def user_profile(request, username):
    return HttpResponse(
        f'User Profile: {username}'
    )


def item_detail(request, item_id):
    return HttpResponse(
        f'Item Id: {item_id}'
    )