from django.test import TestCase
from cars.models import Car, Rate


class CreateCar(TestCase):

    def test_if_can_create_car(self):
        car = Car.objects.create(make='Volkswagen', model='Golf')
        self.assertTrue(car)
        self.assertEqual(car.make, 'Volkswagen')
        self.assertEqual(car.model, 'Golf')


class RateCar(TestCase):
    def setUp(self):
        self.car = Car.objects.create(make='Volkswagen', model='Golf')

    def test_if_can_create_car(self):
        self.assertTrue(self.car)
        rate = Rate.objects.create(car=self.car, rate=4.5)
        self.assertTrue(self.car.rating() == 4.5)
        self.assertTrue(Car.objects.get(rates=rate) == self.car)

    def test_if_rate_range_is_0_to_5(self):
        Rate.objects.create(car=self.car, rate=6)
        self.assertFalse(self.car.rating() == 6)
        self.assertIsNone(self.car.rating())

