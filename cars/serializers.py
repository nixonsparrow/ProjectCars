from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Car, Rate


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Car.objects.all(),
                fields=['make', 'model']
            )
        ]


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
