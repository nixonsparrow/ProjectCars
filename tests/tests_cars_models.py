from django.test import TestCase
from cars.models import Car, Rate


class CreateCarTestCase(TestCase):
    def test_if_can_create_car_object(self):
        car = Car.objects.create(make='Volkswagen', model='Golf')
        self.assertTrue(car)
        self.assertEqual(car.make, 'Volkswagen')
        self.assertEqual(car.model, 'Golf')
        self.assertEqual(Car.objects.all().count(), 1)


class RateTestCase(TestCase):
    def setUp(self):
        self.car = Car.objects.create(make='Volkswagen', model='Golf')

    def test_if_can_create_rate_object(self):
        self.assertTrue(self.car.rate_me(4))

    def test_if_can_rate_car(self):
        rate = self.car.rate_me(4)
        self.assertEqual(Car.objects.get(rates=rate), self.car)

    def test_if_car_avg_rating_is_updating_after_rate_creation(self):
        self.assertIsNone(self.car.avg_rating())
        self.car.rate_me(4)
        self.assertEqual(self.car.avg_rating(), 4.0)


class CarModelMethodsTests(TestCase):
    def setUp(self):
        self.car = Car.objects.create(make='Volkswagen', model='Golf')

    def test_if_avg_rating_is_properly_rounded_to_1st_decimal(self):
        self.assertIsNone(self.car.avg_rating())
        self.car.rate_me(4)
        self.assertEqual(self.car.avg_rating(), 4.0)
        self.car.rate_me(5)
        self.assertEqual(self.car.avg_rating(), 4.5)
        self.car.rate_me(5)
        self.assertEqual(self.car.avg_rating(), 4.7)

    def test_car_rates_number_method(self):
        self.assertEqual(self.car.rates_number(), 0)
        self.car.rate_me(4)
        self.car.rate_me(5)
        self.assertEqual(self.car.rates_number(), 2)
