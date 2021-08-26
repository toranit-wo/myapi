from apis.models import Apis
from apis.serializers import ApisSerializer
from rest_framework import generics


class ApisList(generics.ListCreateAPIView):
    queryset = Apis.objects.all()
    serializer_class = ApisSerializer


class ApisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apis.objects.all()
    serializer_class = ApisSerializer