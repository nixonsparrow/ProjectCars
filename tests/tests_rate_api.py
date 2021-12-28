from rest_framework.test import APITestCase
from django.urls import reverse
from cars.models import Car, Rate


class RatePOSTTestCase(APITestCase):
    def setUp(self):
        self.car = Car.objects.create(make='Volkswagen', model='Golf')

    def test_if_can_post_rate(self):
        self.assertIsNone(self.car.avg_rating())

        new_rate_data = {'car_id': 1, 'rating': 5}
        self.client.post(reverse('add-rate'), new_rate_data, format='json')

        self.assertEqual(self.car.avg_rating(), 5.0)
        self.assertEqual(Rate.objects.all().count(), 1)

    def test_if_cannot_post_rate_if_rate_is_0_or_lower(self):
        response = self.client.post(reverse('add-rate'), {'car_id': self.car.id, 'rating': 0}, format='json')
        self.assertEqual(response.status_code, 400)
        response = self.client.post(reverse('add-rate'), {'car_id': self.car.id, 'rating': -1}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIsNone(self.car.avg_rating())

    def test_if_cannot_post_rate_if_rate_is_6_or_higher(self):
        response = self.client.post(reverse('add-rate'), {'car_id': self.car.id, 'rating': 6}, format='json')
        self.assertEqual(response.status_code, 400)
        response = self.client.post(reverse('add-rate'), {'car_id': self.car.id, 'rating': 99}, format='json')
        self.assertEqual(response.status_code, 400)
