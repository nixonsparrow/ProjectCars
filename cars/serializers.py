import requests
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

    def validate(self, data):
        makes = [a_make['Make_Name'].lower() for a_make in requests.get(
            'https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json').json()['Results']]
        make = data['make'].lower()
        if make not in makes: raise serializers.ValidationError({'make': 'Car Make is not valid.'})

        models = [a_model['Model_Name'].lower() for a_model in requests.get(
            f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json').json()['Results']]
        if data['model'].lower() not in models: raise serializers.ValidationError({'model': 'Car Model is not valid.'})

        return data


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
