import requests
from rest_framework import serializers
from .models import Car, Rate


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

    def validate(self, data):
        make = data['make'].lower()
        model = data['model'].lower()

        if Car.objects.filter(make__iexact=make, model__iexact=model):
            raise serializers.ValidationError('Make + model unique together validation failed.')

        makes = [a_make['Make_Name'].lower() for a_make in requests.get(
            'https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json').json()['Results']]
        if make not in makes: raise serializers.ValidationError({'make': 'Car Make is not valid.'})

        models = [a_model['Model_Name'].lower() for a_model in requests.get(
            f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json').json()['Results']]
        if data['model'].lower() not in models: raise serializers.ValidationError({'model': 'Car Model is not valid.'})

        return data


class PopularCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
