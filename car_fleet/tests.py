from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth import get_user_model
from employee.views import index
from car_fleet import views
from car_fleet.models import Car, Mileage
from datetime import date


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
        self.mileage = Mileage.objects.create(distance=100,
                                              start_day_odometer=0,
                                              end_day_odometer=100,
                                              date=date(2022, 1, 23).strftime('%Y-%m-%d'),
                                              car=self.car
                                              )

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
        self.assertEqual(Car.objects.all().count(), 1)
        self.assertNotEqual(Car.objects.all().count(), 3)
        self.assertContains(response, 'Honda Civic')
        self.assertTemplateUsed(response, 'car_list.html')
        self.assertEqual(match.func.__name__, views.CarListView.as_view().__name__)

    def test_car_detail_view(self):
        response = self.client.get(self.car.get_absolute_url())
        no_response = self.client.get('cars/99/')
        match = resolve('/cars/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'NLI42VN')
        self.assertTemplateUsed(response, 'car_detail.html')
        self.assertEqual(match.func.__name__, views.CarDetailView.as_view().__name__)

    def test_mileage_string_representation(self):
        self.assertEqual(f'{self.mileage.distance}', '100')
        self.assertEqual(f'{self.mileage.start_day_odometer}', '0')
        self.assertEqual(f'{self.mileage.end_day_odometer}', '100')
        self.assertEqual(f'{self.mileage.date}', '2022-01-23')
        self.assertEqual(f'{self.mileage.car}', 'Honda Civic (NLI42VN)')

    def test_mileage_list_view(self):
        response = self.client.get(reverse('car:mileage-list'))
        match = resolve('/cars/mileage/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Mileage.objects.all().count(), 1)
        self.assertNotEqual(Mileage.objects.all().count(), 3)
        self.assertContains(response, 'Mileage list')
        self.assertTemplateUsed(response, 'mileage_list.html')
        self.assertEqual(match.func.__name__, views.MileageListView.as_view().__name__)

    def test_mileage_detail_view(self):
        response = self.client.get(self.mileage.get_absolute_url())
        no_response = self.client.get('cars/mileage/99/')
        match = resolve('/cars/mileage/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Honda Civic')
        self.assertContains(response, 'Distance')
        self.assertTemplateUsed(response, 'mileage_detail.html')
        self.assertEqual(match.func.__name__, views.MileageDetailView.as_view().__name__)