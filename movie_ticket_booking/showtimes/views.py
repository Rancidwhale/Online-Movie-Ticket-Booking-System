from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Theater, Showtime
from .serializers import MovieSerializer, TheaterSerializer, ShowtimeSerializer
# Create your views here.
class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ShowtimeAvailableSeats(generics.RetrieveAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

    def get(self, request, *args, **kwargs):
        showtime = self.get_object()
        available_seats = showtime.available_seats
        return Response({"available_seats": available_seats})

class ReserveSeats(generics.UpdateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        seats_to_reserve = request.data.get('seats_to_reserve')
        if seats_to_reserve > instance.available_seats:
            return Response({"message": "Not enough available seats."}, status=status.HTTP_400_BAD_REQUEST)
        instance.available_seats -= seats_to_reserve
        instance.save()
        return Response({"message": "Seats reserved successfully."})

class PurchaseTickets(generics.UpdateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        tickets_to_purchase = request.data.get('tickets_to_purchase')
        if tickets_to_purchase > instance.available_seats:
            return Response({"message": "Not enough available seats."}, status=status.HTTP_400_BAD_REQUEST)
        instance.available_seats -= tickets_to_purchase
        instance.save()
        return Response({"message": "Tickets purchased successfully."})
