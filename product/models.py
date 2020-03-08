from django.db import models


class Promotion(models.Model):
    name = models.CharField(max_length=128, verbose_name='Promotion name')
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=1.0,
                                   help_text='Describe promotion value i.e. 1 means no promotion, 0.95 means 5% discount')
    start_date = models.DateField()
    end_date = models.DateField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    VAT_VALUES = (
        (1, 0.23),
        (2, 0.08),
        (3, 0.05),
        (4, 0.00),
    )

    name = models.CharField(max_length=128, verbose_name='Product name',
                            help_text='This describe name of specific product')
    net_price = models.DecimalField(max_digits=7, decimal_places=2)
    vat = models.PositiveSmallIntegerField(choices=VAT_VALUES)
    have_promotion = models.BooleanField(default=False)
    packages = models.ForeignKey('Package', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'net_price', 'vat', 'have_promotion', 'packages']

    # nadpisać metodę save(), która zaaktualizuje mi net_price
    def get_discount(self):
        promotion = Promotion.objects.get(product_id=self.id)
        return promotion.discount

    def calculate_net_price(self):
        if self.have_promotion:
            self.net_price *= self.get_discount()
            return self.net_price
        return self.net_price

    def __str__(self):
        return f'{self.name} {self.packages.capacity} {self.packages.capacity_type}'


class Package(models.Model):
    class PackageType(models.Choices):
        JAR = 'Jar'
        FEEDER = 'Feeder'
        PORTION = 'Portion'
        BOTTLE = 'Bottle'
        FOLIC_BAG = 'Folic bag'
        STONEWARE = 'Stoneware'
        TUBE = 'Tube'

    class CapacityType(models.Choices):
        G = 'g'
        L = 'l'

    type = models.CharField(max_length=20, verbose_name='Package type', choices=PackageType.choices)
    capacity = models.PositiveSmallIntegerField(verbose_name='Package weight',
                                                help_text='Weight is measered in grams or liters')
    capacity_type = models.CharField(max_length=1, verbose_name='Package weight type', choices=CapacityType.choices)
    multipack_quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ['type', 'capacity', 'capacity_type', 'multipack_quantity']

    def __str__(self):
        return f'{self.type} {self.capacity} {self.capacity_type}'
