from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from customer.models import Customer, CustomerAddress
from customer.views import CustomerListView, CustomerDetailView, CustomerAddressListView, CustomerAddressDetailView

# Create your tests here.
class CustomerTests(TestCase):
    def setUp(self):
        self.customer_address = CustomerAddress.objects.create(street='Prosta',
                                                               street_number='1',
                                                               city='Warszawa',
                                                               zip_code='01-001')
        self.customer = Customer.objects.create(name='Lidl',
                                                category='CO',
                                                phone_number='501123654',
                                                nip=1234567890,
                                                type='SH',
                                                is_active=True,
                                                addresses=self.customer_address)

    def test_customer_string_representation(self):
        self.assertEqual(f'{self.customer.name}', 'Lidl')
        self.assertEqual(f'{self.customer.category}', 'CO')
        self.assertEqual(f'{self.customer.phone_number}', '501123654')
        self.assertEqual(f'{self.customer.nip}', '1234567890')
        self.assertEqual(f'{self.customer.type}', 'SH')
        self.assertEqual(f'{self.customer.is_active}', 'True')
        self.assertEqual(f'{self.customer.addresses}', 'Prosta 1, Warszawa')

    def test_customer_list_view(self):
        response = self.client.get(reverse('customer:customer-list'))
        match = resolve('/customer/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Customer.objects.all().count(), 1)
        self.assertNotEqual(Customer.objects.all().count(), 2)
        self.assertContains(response, 'Customers:')
        self.assertNotContains(response, 'Nothing to show')
        self.assertTemplateUsed(response, 'customer_list.html')
        self.assertEqual(match.func.__name__, CustomerListView.as_view().__name__)

    def test_customer_detail_view(self):
        response = self.client.get(self.customer.get_absolute_url())
        no_response = self.client.get('/customer/99/')
        match = resolve(self.customer.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Customer detail:')
        self.assertTemplateUsed(response, 'customer_detail.html')
        self.assertEqual(match.func.__name__, CustomerDetailView.as_view().__name__)

    def test_customer_address_string_representation(self):
        self.assertEqual(f'{self.customer_address.street}', 'Prosta')
        self.assertEqual(f'{self.customer_address.street_number}', '1')
        self.assertEqual(f'{self.customer_address.zip_code}', '01-001')
        self.assertEqual(f'{self.customer_address.city}', 'Warszawa')

    def test_customer_address_list_view(self):
        response = self.client.get(reverse('customer:customer-addresses'))
        match = resolve('/customer/address/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CustomerAddress.objects.all().count(), 1)
        self.assertNotEqual(CustomerAddress.objects.all().count(), 3)
        self.assertContains(response, 'Addresses:')
        self.assertNotContains(response, 'Nothing to show')
        self.assertTemplateUsed(response, 'customer_address_list.html')
        self.assertEqual(match.func.__name__, CustomerAddressListView.as_view().__name__)

    def test_customer_address_detail_view(self):
        response = self.client.get(self.customer_address.get_absolute_url())
        no_response = self.client.get('/customer/address/99/')
        match = resolve(self.customer_address.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Address detail:')
        self.assertTemplateUsed(response, 'customer_address_detail.html')
        self.assertEqual(match.func.__name__, CustomerAddressDetailView.as_view().__name__)
