from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Movie, Theater, Showtime


class MovieAPITestCase(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title='Test Movie',
            director='Test Director',
            genre='Test Genre',
            release_date='2022-01-01',
            duration=120,
            synopsis='Test Synopsis'
        )
        self.theater = Theater.objects.create(
            name='Test Theater',
            location='Test Location',
            capacity=100
        )
        self.showtime = Showtime.objects.create(
            movie=self.movie,
            theater=self.theater,
            date_and_time='2022-01-01T12:00:00Z',
            available_seats=100
        )

    def test_movie_list_view(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_movie_detail_view(self):
        url = reverse('movie-detail', kwargs={'pk': self.movie.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_showtime_available_seats_view(self):
        url = reverse('showtime-available-seats', kwargs={'pk': self.showtime.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_reserve_seats_view(self):
        url = reverse('reserve-seats', kwargs={'pk': self.showtime.pk})
        data = {'seats_to_reserve': 5}  # Example: Reserve 5 seats
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_purchase_tickets_view(self):
        url = reverse('purchase-tickets', kwargs={'pk': self.showtime.pk})
        data = {'tickets_to_purchase': 2}  # Example: Purchase 2 tickets
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
