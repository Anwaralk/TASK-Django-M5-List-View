from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer, BookingSerializer




class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer