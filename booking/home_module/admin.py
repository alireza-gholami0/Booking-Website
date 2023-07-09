from django.contrib import admin
from . import models

class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'name', 'terminal_number', 'origin', 'destination', 'departure_date', 'return_date', 'capacity']


class TicketFlightAdmin(admin.ModelAdmin):
    list_display = ['user', 'flight', 'reservation_date', 'quantity']


class TrainAdmin(admin.ModelAdmin):
    list_display = ['train_number', 'name', 'capacity', 'public_facilities', 'origin', 'destination', 'departure_date', 'return_date']


class TrainTicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'train', 'reservation_date', 'quantity', 'coupe_number']


class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'capacity', 'facilities', 'check_in_date', 'check_out_date',]


class HotelReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'hotel', 'reservation_date', 'quantity']

admin.site.register(models.Flight, FlightAdmin)
admin.site.register(models.TicketFlight, TicketFlightAdmin)
admin.site.register(models.Train, TrainAdmin)
admin.site.register(models.TrainTicket, TrainTicketAdmin)
admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.HotelReservation, HotelReservationAdmin)