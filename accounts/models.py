from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.fields import CIEmailField
from django.db import models

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    class RoleType(models.TextChoices):
        DIRECTOR = 'DIR', 'Director'
        MANAGER = 'MAN', 'Manager'
        SALES_AGENT = 'SAG', 'Sales agent'

    class Region(models.TextChoices):
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

    email = CIEmailField(verbose_name='email address',
                         max_length=100,
                         unique=True,
                         error_messages={
                             'unique': 'User with that email already exists'
                         })
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    date_start_job = models.DateField(blank=True, null=True)
    date_end_job = models.DateField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    region = models.CharField(max_length=4,
                              choices=Region.choices,
                              help_text='Determines the area in which the sales agent works',
                              )
    role = models.CharField(max_length=3,
                            choices=RoleType.choices,
                            default=RoleType.SALES_AGENT,
                            help_text='Determines the user role in company')
    phone_number = models.IntegerField(null=True)
    is_active = models.BooleanField(
        verbose_name='account status',
        default=True,
        help_text='Determines if the user has an active account'
    )
    admin = models.BooleanField(
        verbose_name='admin status',
        default=False,
        help_text='Determines if the user is superuser and can manage the admin panel'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.email

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.get_full_name()

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.admin
