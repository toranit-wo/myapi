from apis.models import Apis
from apis.serializers import ApisSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ApisList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        apis = Apis.objects.all()
        serializer = ApisSerializer(apis, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApisDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Apis.objects.get(pk=pk)
        except Apis.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        apis = self.get_object(pk)
        serializer = ApisSerializer(apis)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        apis = self.get_object(pk)
        serializer = ApisSerializer(apis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        apis = self.get_object(pk)
        apis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)