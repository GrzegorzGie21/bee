from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from django.urls import resolve
from employee.views import index


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
