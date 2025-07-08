from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("Welcome to Little Lemon API")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/', include('bookings.urls')),
    path('', include('restaurant.urls')),


    # Djoser user management (registration, password reset, etc.)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),


    # JWT token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
