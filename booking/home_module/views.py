from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from account_module.models import User
from home_module import serializers
from home_module.models import Flight, Hotel, Train, TicketFlight
from home_module.serializers import FlightSerializer, HotelSerializer, TrainSerializer, TicketFlightSerializer


# Create your views here.
def home(request):
    return render(request, 'home_module/home.html')

class FlightSearchAPIView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_queryset(self):
        queryset = Flight.objects.all()

        origin = self.request.query_params.get('origin', default=None)
        destination = self.request.query_params.get(key='destination',default=None)
        departure_date = self.request.query_params.get('departure_date',default= None)
        return_date = self.request.query_params.get('return_date', default=None)
        capacity = self.request.query_params.get('capacity', None)
        print(self.request.query_params)

        if origin is not None:
            queryset = queryset.filter(origin__icontains=origin)


        if destination is not None:
            queryset = queryset.filter(destination__icontains=destination)

        if departure_date is not None:
            queryset = queryset.filter(departure_date__date=departure_date)

        if return_date is not None:
            queryset = queryset.filter(return_date__date=return_date)
        if capacity is not None:
            queryset = queryset.filter(capacity__gte=capacity)

        return queryset

class HotelSearchAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_queryset(self):
        queryset = Hotel.objects.all()

        city = self.request.query_params.get('city', None)
        check_in_date = self.request.query_params.get('check_in_date', None)
        check_out_date = self.request.query_params.get('check_out_date', None)
        capacity = self.request.query_params.get('capacity', None)

        if city is not None:
            queryset = queryset.filter(city__icontains=city)

        if check_in_date is not None:
            queryset = queryset.filter(check_in_date__date=check_in_date)

        if check_out_date is not None:
            queryset = queryset.filter(check_out_date__date=check_out_date)
        if capacity is not None:
            queryset = queryset.filter(capacity__gte=capacity)

        return queryset

class TrainSearchAPIView(generics.ListAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def get_queryset(self):
        queryset = Train.objects.all()

        origin = self.request.query_params.get('origin', None)
        destination = self.request.query_params.get('destination', None)
        departure_date = self.request.query_params.get('departure_date', None)
        return_date = self.request.query_params.get('return_date', None)
        capacity = self.request.query_params.get('capacity', None)

        if origin is not None:
            queryset = queryset.filter(origin__icontains=origin)

        if destination is not None:
            queryset = queryset.filter(destination__icontains=destination)

        if departure_date is not None:
            queryset = queryset.filter(departure_date__date=departure_date)

        if return_date is not None:
            queryset = queryset.filter(return_date__date=return_date)
        if capacity is not None:
            queryset = queryset.filter(capacity__gte=capacity)
        return queryset

class ReserveFlightTicketView(APIView):
    def post(self, request):
        flight_id = request.data.get('flight_id')
        national_code = request.data.get('national_code')
        gender = request.data.get('gender')
        phone_number = request.data.get('phone_number')
        full_name = request.data.get('full_name')
        quantity = request.data.get('quantity')
        if not request.user.is_authenticated:
            return Response({"error": "Not Authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
        if not all([flight_id, national_code, gender, phone_number, full_name, quantity]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        if request.user.national_code != national_code or request.user.gender != gender \
                or request.user.phone_number != phone_number or request.user.get_full_name() != full_name:
            return Response({"error": "User information does not match."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            flight = Flight.objects.get(pk=flight_id)
            if flight.capacity < quantity:
                return Response({"error": "Not enough capacity."}, status=status.HTTP_400_BAD_REQUEST)
            ticket_flight = TicketFlight.objects.create(user=request.user, flight=flight, quantity=quantity)
            serializer = TicketFlightSerializer(ticket_flight)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Flight.DoesNotExist:
            return Response({"error": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)