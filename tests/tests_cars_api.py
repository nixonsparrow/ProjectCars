from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from django.urls import reverse
from cars.views import car_list


class CarsGetTestCase(APITestCase):
    def test_get_car_list_in_json(self):
        factory = APIRequestFactory()
        response = car_list(factory.get(reverse('car-list')))
        self.assertEqual(response.status_code, 200)
