from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from product.models import Package, Product, Promotion
from product import views

from datetime import date


# Create your tests here.
class PackageTests(TestCase):
    def setUp(self):
        self.package = Package.objects.create(type='Jar', capacity_type='l', capacity=1, multipack_quantity=8)

    def test_package_string_representation(self):
        self.assertEqual(f'{self.package.type}', 'Jar')
        self.assertEqual(f'{self.package.get_capacity_type_display()}', 'Litre')
        self.assertEqual(f'{self.package.capacity}', '1')
        self.assertEqual(f'{self.package.multipack_quantity}', '8')

    def test_package_list_view(self):
        response = self.client.get(reverse('product:package-list'))
        match = resolve('/product/package/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Package.objects.all().count(), 1)
        self.assertNotEqual(Package.objects.all().count(), 2)
        self.assertContains(response, 'Packages:')
        self.assertNotContains(response, 'This is invalid content')
        self.assertTemplateUsed(response, 'package_list.html')
        self.assertEqual(match.func.__name__, views.PackageListView.as_view().__name__)

    def test_package_detail_view(self):
        response = self.client.get(self.package.get_absolute_url())
        no_response = self.client.get('/product/package/88/')
        match = resolve(self.package.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Capacity Type:')
        self.assertNotContains(response, 'This is invalid content')
        self.assertTemplateUsed(response, 'package_detail.html')
        self.assertEqual(match.func.__name__, views.PackageDetailView.as_view().__name__)


class PromotionTests(TestCase):
    def setUp(self):
        self.promotion = Promotion.objects.create(name='New Year',
                                                  discount=0.8,
                                                  start_date=date(2022, 1, 1).strftime('%Y-%m-%d'),
                                                  end_date=date(2022, 2, 28).strftime('%Y-%m-%d'))

    def test_promotion_string_representation(self):
        self.assertEqual(f'{self.promotion.name}', 'New Year')
        self.assertEqual(f'{self.promotion.discount}', '0.8')
        self.assertEqual(f'{self.promotion.start_date}', '2022-01-01')
        self.assertEqual(f'{self.promotion.end_date}', '2022-02-28')

    def test_promotion_list_view(self):
        response = self.client.get(reverse('product:promotion-list'))
        match = resolve('/product/promotion/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Promotion.objects.all().count(), 1)
        self.assertNotEqual(Promotion.objects.all().count(), 2)
        self.assertContains(response, 'Promotion list:')
        self.assertNotContains(response, 'This is invalid content')
        self.assertTemplateUsed(response, 'promotion_list.html')
        self.assertEqual(match.func.__name__, views.PromotionListView.as_view().__name__)

    def test_promotion_detail_view(self):
        response = self.client.get(self.promotion.get_absolute_url())
        no_response = self.client.get('/product/promotion/88/')
        match = resolve(self.promotion.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Promotion detail')
        self.assertNotContains(response, 'This is invalid content')
        self.assertTemplateUsed(response, 'promotion_detail.html')
        self.assertEqual(match.func.__name__, views.PromotionDetailView.as_view().__name__)


class ProductTests(TestCase):
    def setUp(self):
        self.promotion = Promotion.objects.create(name='New Year',
                                                  discount=0.8,
                                                  start_date=date(2022, 1, 1).strftime('%Y-%m-%d'),
                                                  end_date=date(2022, 2, 28).strftime('%Y-%m-%d'))
        self.package = Package.objects.create(type='Jar', capacity_type='l', capacity=1, multipack_quantity=8)
        self.product = Product.objects.create(name='Lime honey',
                                              net_price=13.50,
                                              vat=1,
                                              have_promotion=True,
                                              promotion=self.promotion,
                                              packages=self.package)

    def test_product_string_representation(self):
        self.assertEqual(f'{self.product.name}', 'Lime honey')
        self.assertEqual(f'{self.product.net_price}', '13.5')
        self.assertEqual(f'{self.product.get_vat_display()}', '0.23')
        self.assertEqual(f'{self.product.have_promotion}', 'True')
        self.assertEqual(f'{self.product.promotion}', 'New Year')
        self.assertEqual(f'{self.product.packages}', 'Jar 1 l')

    def test_product_list_view(self):
        response = self.client.get(reverse('product:product-list'))
        match = resolve('/product/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertNotEqual(Product.objects.all().count(), 2)
        self.assertContains(response, 'Product list:')
        self.assertNotContains(response, 'This is invalid content')
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertEqual(match.func.__name__, views.ProductListView.as_view().__name__)

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/product/88/')
        match = resolve(self.product.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Product detail')
        self.assertNotContains(response, 'This is invalid content')
        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertEqual(match.func.__name__, views.ProductDetailView.as_view().__name__)
