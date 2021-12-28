from rest_framework.test import APITestCase
from django.urls import reverse
from cars.models import Car
import json


class PopularTestCase(APITestCase):
    def setUp(self):
        self.cars_and_rates = [
            ({'make': 'Volkswagen', 'model': 'Golf'}, [2, 2, 4, 4, 5, 6]),
            ({'make': 'Volkswagen', 'model': 'Passat'}, [3, 2, 5, 4, 6]),
            ({'make': 'Fiat', 'model': 'Ducato'}, [1, 2, 3, 4, 5, 6, 3, 2, 1]),
            ({'make': 'Fiat', 'model': 'Brava'}, [1, 2, 3, 4, 5, 6]),
            ({'make': 'Toyota', 'model': 'Corolla'}, [1, 2, 3, 4, 5, 6]),
            ({'make': 'Toyota', 'model': 'Yaris'}, [1, 2, 3, 4, 5, 6]),
            ({'make': 'Dodge', 'model': 'Viper'}, [6, 6, 6]),
            ({'make': 'Porsche', 'model': 'Cayenne'}, [5, 6, 6, 5])
        ]

        for car, rates in self.cars_and_rates:
            car_object = Car.objects.create(make=car['make'], model=car['model'])
            [car_object.rate_me(rate) for rate in rates]

    def test_if_setup_is_correct(self):
        self.assertEqual(Car.objects.all().count(), len(self.cars_and_rates))
        self.assertEqual(sum([len(rates) for car, rates in self.cars_and_rates]), 45)

    def test_if_popular_url_gives_proper_response(self):
        response = self.client.get(reverse('car-popular'))
        self.assertEqual(response.status_code, 200)

    def test_if_popular_url_calculates_rates_number(self):
        response = self.client.get(reverse('car-popular'))
        for car_dict in json.loads(response.content):
            car = Car.objects.get(id=car_dict['id'])
            self.assertEqual(car_dict['rates_number'], car.rates_number())
