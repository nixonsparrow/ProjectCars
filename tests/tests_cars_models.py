from django.test import TestCase
from cars.models import Car, Rate


class CreateCarTestCase(TestCase):

    def test_if_can_create_car_object(self):
        car = Car.objects.create(make='Volkswagen', model='Golf')
        self.assertTrue(car)
        self.assertEqual(car.make, 'Volkswagen')
        self.assertEqual(car.model, 'Golf')


class RateTestCase(TestCase):
    def setUp(self):
        self.car = Car.objects.create(make='Volkswagen', model='Golf')

    def test_if_can_create_rate_object(self):
        self.assertTrue(Rate.objects.create(car=self.car, rate=4))

    def test_if_can_rate_car(self):
        rate = Rate.objects.create(car=self.car, rate=4)
        self.assertEqual(Car.objects.get(rates=rate), self.car)


class CarModelMethodsTests(TestCase):
    def setUp(self):
        self.car = Car.objects.create(make='Volkswagen', model='Golf')

    def test_if_rating_is_properly_rounded_to_1st_decimal(self):
        self.assertIsNone(self.car.rating())
        Rate.objects.create(car=self.car, rate=4)
        Rate.objects.create(car=self.car, rate=5)
        self.assertEqual(self.car.rating(), 4.5)

    def test_total_votes_method(self):
        self.assertEqual(self.car.total_votes(), 0)
        Rate.objects.create(car=self.car, rate=4)
        Rate.objects.create(car=self.car, rate=5)
        self.assertEqual(self.car.total_votes(), 2)

    # def test_if_rate_range_is_0_to_5(self):
        # self.assertIsNone(self.car.rating())
        # Rate.objects.create(car=self.car, rate=6)
        # self.assertFalse(self.car.rating() == 6)

