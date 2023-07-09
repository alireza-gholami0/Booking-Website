from rest_framework import serializers
from .models import Flight, TicketFlight, Train, TrainTicket, Hotel, HotelReservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class TicketFlightSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)
    flight_id = serializers.PrimaryKeyRelatedField(source='flight', queryset=Flight.objects.all(), write_only=True)

    class Meta:
        model = TicketFlight
        fields = ('id', 'user', 'flight_id', 'flight', 'reservation_date', 'quantity')

    def create(self, validated_data):
        user = self.context['request'].user
        flight = validated_data['flight']
        quantity = validated_data['quantity']
        ticket_flight = TicketFlight.objects.create(user=user, flight=flight, quantity=quantity)
        return ticket_flight


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'


class TrainTicketSerializer(serializers.ModelSerializer):
    train = TrainSerializer(read_only=True)
    train_id = serializers.PrimaryKeyRelatedField(source='train', queryset=Train.objects.all(), write_only=True)

    class Meta:
        model = TrainTicket
        fields = ('id', 'user', 'train_id', 'train', 'reservation_date', 'quantity', 'coupe_number')

    def create(self, validated_data):
        user = self.context['request'].user
        train = validated_data['train']
        quantity = validated_data['quantity']
        coupe_number = validated_data['coupe_number']
        train_ticket = TrainTicket.objects.create(user=user, train=train, quantity=quantity,coupe_number=coupe_number)
        return train_ticket


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelReservationSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)
    hotel_id = serializers.PrimaryKeyRelatedField(source='hotel', queryset=Hotel.objects.all(), write_only=True)

    class Meta:
        model = HotelReservation
        fields = ('id', 'user', 'hotel_id', 'hotel', 'reservation_date', 'quantity')

    def create(self, validated_data):
        user = self.context['request'].user
        hotel = validated_data['hotel']
        quantity = validated_data['quantity']
        hotel_reservation = HotelReservation.objects.create(
            user=user, hotel=hotel, quantity=quantity
        )
        return hotel_reservation


class ValidationError(Exception):
    pass