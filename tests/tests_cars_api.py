from rest_framework.test import APITestCase
from django.urls import reverse
from cars.models import Car


class CarsGETTestCase(APITestCase):
    def setUp(self):
        pass

    def test_get_car_list_in_json(self):
        response = self.client.get(reverse('car-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_get_car_list_in_json_count_before_and_after_adding_new_car(self):
        response = self.client.get(reverse('car-list'))
        self.assertEqual(len(response.data), 0)

        Car.objects.create(make='Volkswagen', model='Golf')

        response = self.client.get(reverse('car-list'))
        self.assertEqual(len(response.data), 1)
        self.assertIn("[('id', 1), ('make', 'Volkswagen'), ('model', 'Golf'), ('avg_rating', None)]", response.data.__str__())


class CarsPOSTTestCase(APITestCase):
    def setUp(self):
        pass

    def test_cars_post_add_car_to_database(self):
        # POST data with new car - valid example
        new_car_data = {'make': 'Volkswagen', 'model': 'Passat'}
        print('CAR:', Car.objects.first())
        self.client.post(reverse('car-list'), new_car_data, format='json')
        print('CAR:', Car.objects.first())

        # assert new car with GET view and db check
        self.assertEqual(len(self.client.get(reverse('car-list')).data), 1)
        self.assertEqual(Car.objects.all().count(), 1)

    def test_if_not_able_to_post_non_existing_make(self):
        wrong_make_car_data = {'make': 'Volkswaaaaagen', 'model': 'Passat'}
        response = self.client.post(reverse('car-list'), wrong_make_car_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_if_not_able_to_post_non_existing_model(self):
        wrong_model_car_data = {'make': 'Volkswagen', 'model': 'Passssssssssat'}
        response = self.client.post(reverse('car-list'), wrong_model_car_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_if_not_able_to_post_same_make_plus_model_that_is_already_in_db(self):
        new_car_data = {'make': 'Volkswagen', 'model': 'Passat'}
        # POST data with new car twice - valid example
        response = self.client.post(reverse('car-list'), new_car_data, format='json')
        self.assertEqual(response.status_code, 201)
        # second one returns error - not unique object
        response = self.client.post(reverse('car-list'), new_car_data, format='json')
        self.assertEqual(response.status_code, 400)


class CarsDELETETestCase(APITestCase):
    def setUp(self):
        pass

    def test_if_404_if_try_to_delete_non_existing_car(self):
        response = self.client.delete(reverse('car-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 404)

    def test_if_can_delete_car(self):
        Car.objects.create(make='Volkswagen', model='Passat')
        response = self.client.delete(reverse('car-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 204)
