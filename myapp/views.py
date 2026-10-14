
# from django.http import HttpResponse


# # Q3
# def filter_movies(request):
#     genre = request.GET.get('genre')
#     year = request.GET.get('year')

#     return HttpResponse(f"Genre: {genre}, Year: {year}")


# # Q4 - Movie
# def movie_view(request, movie_name):
#     return HttpResponse(f"Movie: {movie_name}")


# # Q4 - Screen
# def screen_view(request, screen_no):
#     return HttpResponse(f"Screen Number: {screen_no}")


# # Q4 - Booking
# def booking_view(request, booking_id):
#     return HttpResponse(f"Booking ID: {booking_id}")


# # Q4 - Search
# def search_view(request):
#     city = request.GET.get('city')
#     date = request.GET.get('date')

#     return HttpResponse(f"City: {city}, Date: {date}")




# def about(request):
#     context={
#         "name": "Rahul",
#         "Age": 19,
#         "Course": "B-tech_CSE",
#         "City": "Phagwara"
#     }

#     return render(request, "about.html", context)

from django.shortcuts import render


def home(request):
    dishes = [
        {
            'name': 'Burger',
            'description': 'Juicy burger with fresh veggies and sauce',
            'price': 199,
            'image': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=80',
        },
        {
            'name': 'Pizza',
            'description': 'Classic delight with fresh basil & cheese',
            'price': 249,
            'image': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=900&q=80',
        },
        {
            'name': 'Veg Sandwich',
            'description': 'Fresh veggies wrapped in soft bread',
            'price': 149,
            'image': 'https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=900&q=80',
        },
        {
            'name': 'Chocolate Lava',
            'description': 'Warm chocolate cake with a molten center',
            'price': 179,
            'image': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=900&q=80',
        },
        {
            'name': 'Cheese Paneer',
            'description': 'Soft paneer cubes in rich cheesy gravy',
            'price': 219,
            'image': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=900&q=80',
        },
        {
            'name': 'Creamy Pasta',
            'description': 'Rich creamy sauce with herbs and parmesan',
            'price': 229,
            'image': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?auto=format&fit=crop&w=900&q=80',
        },
    ]
    return render(request, 'home.html', {'dishes': dishes})


def about(request):
    return render(request, 'about.html')