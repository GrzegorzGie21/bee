from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.db.models import Sum


class Order(models.Model):
    number = models.CharField(max_length=20, default='0')
    date = models.DateField()
    products = models.ManyToManyField('product.Product', through='OrderProducts')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    customer = models.ForeignKey('customer.Customer', default='Customer does not exist', on_delete=models.SET_DEFAULT)

    # nadpisać metodę save(). która mi zaaktualizuje number
    def calculate_number(self):
        return str(self.user_id) + '/' + str(self.customer_id) + '/' + str(self.date.month) + '/' + str(self.date.year)

    def __str__(self):
        return f'{self.date} by {self.user.last_name}'

    def summary_quantity(self):
        return self.products.aggregate(Sum('quantity'))

    def get_absolute_url(self):
        return reverse('order:order-detail', kwargs={'pk': self.pk})


class OrderProducts(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Product {self.product.name} with {self.quantity} units'
