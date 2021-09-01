from apis.models import Forehand,Backhand
from apis.serializers import ForehandSerializer,BackhandSerializer
from rest_framework import generics


class ForehandList(generics.ListCreateAPIView):
    queryset = Forehand.objects.all()
    serializer_class = ForehandSerializer


class ForehandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forehand.objects.all()
    serializer_class = ForehandSerializer

class BackhandList(generics.ListCreateAPIView):
    queryset = Backhand.objects.all()
    serializer_class = BackhandSerializer


class BackhandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Backhand.objects.all()
    serializer_class = BackhandSerializer

