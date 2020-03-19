from django.db import models
# from product.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    number = models.CharField(max_length=20, default='0')
    date = models.DateField()
    products = models.ManyToManyField('product.Product', through='OrderProducts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)

    # nadpisać metodę save(). która mi zaaktualizuje number
    def calculate_number(self):
        return str(self.user_id) + '/' + str(self.customer_id) + '/' + str(self.date.month) + '/' + str(self.date.year)

    def __str__(self):
        return f'{self.date} by {self.user.last_name}'


class OrderProducts(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Product {self.product.name} with {self.quantity} units'