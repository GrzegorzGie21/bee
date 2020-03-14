from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Document(models.Model):
    class DocumentType(models.TextChoices):
        CASH = 'C'
        NO_CASH = 'N'

    title = models.CharField(max_length=50, verbose_name='Document title')
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    created_date = models.DateField(verbose_name='Document created day')
    type = models.CharField(max_length=1, choices=DocumentType.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    class WorkStationType(models.TextChoices):
        DIRECTOR = 'DIR', 'Director'
        MANAGER = 'MAN', 'Manager'
        SALES_AGENT = 'SAG', 'Sales agent'

    class RegionName(models.TextChoices):
        DOLNOSLASKIE = 'DSL'
        KUJAWSKO_POMORSKIE = 'K-P'
        LUBELSKIE = 'LBL'
        LUBUSKIE = 'LBU'
        LODZKIE = 'LDZ'
        MALOPOLSKIE = 'MLP'
        MAZOWIECKIE = 'MAZ'
        OPOLSKIE = 'OPO'
        PODKARPACKIE = 'PKR'
        PODLASKIE = 'PDL'
        POMORSKIE = 'POM'
        SLASKIE = 'SL'
        SWIETOKRZYSKIE = 'SW'
        WARMINSKO_MAZURSKIE = 'W-M'
        WIELKOPOLSKIE = 'WLKP'
        ZACHODNIOPOMORSKIE = 'ZPM'

    work_station = models.CharField(max_length=3, choices=WorkStationType.choices, default=WorkStationType.SALES_AGENT)
    region = models.CharField(max_length=4, choices=RegionName.choices)
    phone_number = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.work_station} {self.user.last_name}'
