from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    re_path(
        r'^user/(?P<username>[a-zA-Z]+)/$',
        views.user_profile
    ),

    re_path(
        r'^item/(?P<item_id>\d+)/$',
        views.item_detail
    ),
]