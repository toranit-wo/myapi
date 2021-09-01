from rest_framework import serializers
from apis.models import Backhand, Forehand
import json
import numpy as np
from scipy.signal import find_peaks

class ForehandSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id',
            'hits',
            'over',
            'under',
            'good',
        ]
        model = Forehand

        def create(self, validated_data):

            return Forehand.objects.create(**validated_data)

        def update(self, instance, validated_data):

            instance.title = validated_data.get('title', instance.title)
            instance.data = validated_data.get('data', instance.data)
            instance.save()
            return instance

class BackhandSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'hits',
            'over',
            'under',
            'good',
        )
        model = Backhand

        def create(self, validated_data):

            return Forehand.objects.create(**validated_data)

        def update(self, instance, validated_data):

            instance.title = validated_data.get('title', instance.title)
            instance.data = validated_data.get('data', instance.data)
            instance.save()
            return instance



