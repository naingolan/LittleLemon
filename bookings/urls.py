from django.urls import path
from .views import BookingListCreate, BookingRetrieveUpdateDestroy, UserCreate

urlpatterns = [
    path('bookings/', BookingListCreate.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroy.as_view(), name='booking-detail'),
    path('registration/', UserCreate.as_view(), name='user-registration'),
]