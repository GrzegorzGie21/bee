from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomerAddress(models.Model):
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=6)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.street} {self.street_number}, {self.city}'


class Customer(models.Model):
    class CustomerCategory(models.TextChoices):
        SELF_SERVICE_OVER_2_CHECKOUTS = 'SSO2', _('Self service shop over 2 checkouts')
        SELF_SERVICE_UNDER_2_CHECKOUTS = 'SSU2', _('Self service shop under 2 checkouts')
        COUNTER = 'CO', _('Counter shop')

    class CustomerType(models.TextChoices):
        WHOLESALER = 'WH'
        SHOP = 'SH'

    name = models.CharField(max_length=128, verbose_name='Customer name')
    category = models.CharField(max_length=4, verbose_name='Customer category',
                                choices=CustomerCategory.choices, default=CustomerCategory.COUNTER)
    phone_number = models.PositiveIntegerField()
    nip = models.PositiveIntegerField()
    type = models.CharField(max_length=2, verbose_name='Customer type',
                            choices=CustomerType.choices, default=CustomerType.SHOP)
    is_active = models.BooleanField(default=True)
    addresses = models.OneToOneField(CustomerAddress, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
