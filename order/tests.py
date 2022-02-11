from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth import get_user_model

from order.models import Order, OrderProducts
from customer.models import Customer, CustomerAddress
from order import views
from django.contrib.auth.models import Permission

from datetime import date


# Create your tests here.
class OrderTests(TestCase):
    def setUp(self):
        self.permission = Permission.objects.get(codename='add_order')
        self.user = get_user_model().objects.create_user(username='grzegorz', password='haslo123')
        self.customer_address = CustomerAddress.objects.create(street='Prosta',
                                                               street_number=1,
                                                               zip_code='01-001',
                                                               city='Warszawa')
        self.customer = Customer.objects.create(name='Lidl',
                                                category='CO',
                                                phone_number='501123654',
                                                nip=1234567890,
                                                type='SH',
                                                is_active=True,
                                                addresses=self.customer_address)
        self.order = Order.objects.create(number=12,
                                          date=date(2022, 1, 13).strftime('%Y-%m-%d'),
                                          user=self.user,
                                          customer=self.customer
                                          )

    def test_order_string_representation(self):
        self.assertEqual(f'{self.order.number}', '12')
        self.assertEqual(f'{self.order.date}', '2022-01-13')
        self.assertEqual(f'{self.order.user}', 'grzegorz')
        self.assertEqual(f'{self.order.customer}', 'Lidl')

    def test_order_list_view(self):
        response = self.client.get(reverse('order:order-list'))
        match = resolve('/order/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.all().count(), 1)
        self.assertNotEqual(Order.objects.all().count(), 5)
        self.assertContains(response, 'Order list:')
        self.assertNotContains(response, 'Empty page')
        self.assertTemplateUsed(response, 'order_list.html')
        self.assertEqual(match.func.__name__, views.OrderListView.as_view().__name__)

    def test_order_detail_view(self):
        response = self.client.get(self.order.get_absolute_url())
        no_response = self.client.get('/order/77/')
        match = resolve(self.order.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Order nr' and 'Products:')
        self.assertNotContains(response, 'Empty page')
        self.assertTemplateUsed(response, 'order_detail.html')
        self.assertEqual(match.func.__name__, views.OrderDetailView.as_view().__name__)

    def test_order_edit_view(self):
        response = self.client.get(reverse('order:edit-order', args=[self.order.pk]))
        no_response = self.client.get('order/88/edit/')
        match = resolve('/order/1/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Edit order')
        self.assertTemplateUsed(response, 'order_update.html')
        self.assertEqual(match.func.__name__, views.OrderUpdateView.as_view().__name__)

    def test_order_delete_view(self):
        response = self.client.get(reverse('order:delete-order', args=[self.order.pk]))
        no_response = self.client.get('/order/88/delete/')
        match = resolve('/order/1/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Delete order')
        self.assertTemplateUsed(response, 'order_delete.html')
        self.assertEqual(match.func.__name__, views.OrderDeleteView.as_view().__name__)

    def test_order_create_view(self):
        self.client.login(username='grzegorz', password='haslo123')
        self.user.user_permissions.add(self.permission)
        response = self.client.get(reverse('order:add-order'))
        match = resolve('/order/add/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add order:')
        self.assertTemplateUsed(response, 'order_add.html')
        self.assertEqual(match.func.__name__, views.OrderAddView.as_view().__name__)
