from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from account_module.models import User


class Flight(models.Model):
    flight_number = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    terminal_number = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destination} ({self.flight_number})"

class TicketFlight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f"{self.user.email} - {self.flight.flight_number}"


class Train(models.Model):
    train_number = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    public_facilities = models.TextField()
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.origin} - {self.destination} ({self.train_number})"

class TrainTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(blank=True, null=True)
    coupe_number = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"{self.user.email} - {self.train.train_number}"

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    capacity = models.IntegerField()
    facilities = models.TextField()
    check_in_date = models.DateTimeField(null=True)
    check_out_date = models.DateTimeField(null=True)
    def __str__(self):
        return f"{self.name} - {self.city}"

class HotelReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    reservation_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user.email} - {self.hotel.name}"