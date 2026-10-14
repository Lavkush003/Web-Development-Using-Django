from django.urls import path, re_path
from . import views

# urlpatterns = [
#     # Q3
#     path('filter/', views.filter_movies),

#     # Q4
#     path('movie/<str:movie_name>/', views.movie_view),

#     path('screen/<int:screen_no>/', views.screen_view),

#     re_path(r'^booking/(BK\d{4})/$', views.booking_view),

#     path('search/', views.search_view),
# ]

from django.urls import path
from .views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]