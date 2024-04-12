"""
URL configuration for movie_ticket_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from showtimes import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/movies/', views.MovieList.as_view(), name='movie-list'),
    path('api/movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('api/showtimes/<int:showtime_id>/seats/', views.ShowtimeAvailableSeats.as_view(), name='showtime-seats'),
    path('api/showtimes/<int:showtime_id>/reserve/', views.ReserveSeats.as_view(), name='reserve-seats'),
    path('api/reservations/<int:reservation_id>/purchase/', views.PurchaseTickets.as_view(), name='purchase-tickets')
]

