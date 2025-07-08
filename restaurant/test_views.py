from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(name="Pizza", description="Cheese pizza", price=9.99)

    def test_get_menu_list(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class BookingViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Booking.objects.create(name="John Doe", email="john@example.com", date="2025-07-08", time="18:00:00", guests=4)

    def test_get_booking_list(self):
        response = self.client.get(reverse('booking-list'))
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)