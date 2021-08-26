from rest_framework import serializers
from apis.models import Apis,Forehand,Backhand


class ApisSerializer(serializers.Serializer):
    class Meta:
        model = Apis
        fields = ['id', 'title', 'data']

    def create(self, validated_data):
        """
        Create and return a new `Apis` instance, given the validated data.
        """
        return Apis.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Apis` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.data = validated_data.get('data', instance.data)
        instance.save()
        return instance