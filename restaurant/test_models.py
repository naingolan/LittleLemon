from django.test import TestCase
from .models import Menu, Booking

class MenuModelTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Pizza", description="Cheese pizza", price=9.99)

    def test_menu_creation(self):
        menu = Menu.objects.get(name="Pizza")
        self.assertEqual(menu.description, "Cheese pizza")
        self.assertEqual(menu.price, 9.99)

class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(name="John Doe", email="john@example.com", date="2025-07-08", time="18:00:00", guests=4)

    def test_booking_creation(self):
        booking = Booking.objects.get(name="John Doe")
        self.assertEqual(booking.email, "john@example.com")
        self.assertEqual(booking.guests, 4)