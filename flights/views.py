from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer, BookingSerializer
from django.utils import timezone



class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingSerializer


    