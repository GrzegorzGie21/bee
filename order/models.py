from django.db import models
# from product.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    number = models.CharField(max_length=20, default='0')
    date = models.DateField()
    products = models.ManyToManyField('product.Product', through='OrderProducts')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.OneToOneField('customer.Customer', on_delete=models.CASCADE)

    # nadpisać metodę save(). która mi zaaktualizuje number
    def calculate_number(self):
        return str(self.pk) + '/' + str(self.date.month) + '/' + str(self.date.year)


class OrderProducts(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()