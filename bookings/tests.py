from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Booking

class BookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.client.login(username='testuser', password='pass1234')

    def test_create_booking(self):
        url = reverse('booking-list-create')
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890",
            "date": "2025-07-15",
            "time": "19:00:00",
            "guests": 4
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
