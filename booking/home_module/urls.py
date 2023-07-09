from django.urls import path
from . import views
from .views import FlightSearchAPIView



urlpatterns = [
    path('', views.home, name='home'),
    path('api/flights/search/', FlightSearchAPIView.as_view(), name='flight_search_api'),
    path('api/trains/search/', FlightSearchAPIView.as_view(), name='train_search_api'),
    path('api/hotels/search/', views.HotelSearchAPIView.as_view(), name='hotel_search_api'),
    path('reserve-flight-ticket/', views.ReserveFlightTicketView.as_view(), name='reserve_flight_ticket'),
]
