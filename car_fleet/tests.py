from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth import get_user_model
from employee.views import index
from car_fleet.views import CarListView, CarDetailView
from car_fleet.models import Car, Mileage


# Create your tests here.

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_contains_correct_content(self):
        self.assertContains(self.response, 'Order and report app')

    def test_home_page_does_not_contains_incorrect_content(self):
        self.assertNotContains(self.response, 'Hello')

    def test_home_page_use_correct_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_page_url_resolve_home_page_view(self):
        match = resolve('/')
        self.assertEqual(match.func.__name__, index.__name__)


class CarTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='grzegorz',
                                                         password='pass1234')
        self.car = Car.objects.create(manufacturer='Honda',
                                      model='Civic',
                                      registration_number='NLI42VN',
                                      manufacture_year=2_002,
                                      engine_power=90,
                                      engine_size=1.4,
                                      user=self.user,
                                      odometer=100_000)

    def test_car_listing(self):
        self.assertEqual(f'{self.car.manufacturer}', 'Honda')
        self.assertEqual(f'{self.car.model}', 'Civic')
        self.assertEqual(f'{self.car.registration_number}', 'NLI42VN')
        self.assertEqual(f'{self.car.manufacture_year}', '2002')
        self.assertEqual(f'{self.car.engine_power}', '90')
        self.assertEqual(f'{self.car.engine_size}', '1.4')
        self.assertEqual(f'{self.car.user}', 'grzegorz')
        self.assertEqual(f'{self.car.odometer}', '100000')

    def test_car_list_view(self):
        response = self.client.get(reverse('car:car-list'))
        match = resolve('/cars/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Honda Civic')
        self.assertTemplateUsed(response, 'car_list.html')
        self.assertEqual(match.func.__name__, CarListView.as_view().__name__)

    def test_car_detail_view(self):
        response = self.client.get(reverse(self.car.get_absolute_url))
        match = resolve('/cars/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Honda Civic')
        self.assertTemplateUsed(response, 'car_detail.html')
        self.assertEqual(match.func.__name__, CarDetailView.as_view().__name__)
