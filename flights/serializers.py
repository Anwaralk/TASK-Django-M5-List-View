from .views import Flight, Booking
from rest_framework import serializers



class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        List = ['id', 'destination', 'time', 'price']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        List = ['id', 'flight', 'date']