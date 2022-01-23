from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Car(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=7)
    manufacture_year = models.PositiveSmallIntegerField()
    engine_power = models.PositiveSmallIntegerField(help_text='Power is measured in horse power')
    engine_size = models.DecimalField(max_digits=2, decimal_places=1, help_text='Size is measured in cm3')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    odometer = models.PositiveIntegerField(default=0)

    # tutaj nadpisanie funckcji save(), ktora mi zaktualizuje odometer

    def update_odometer(self):
        self.odometer = Mileage.objects.filter(car_id=self.pk).order_by('-date').first().end_day_odometer
        return self.odometer

    def __str__(self):
        return f'{self.manufacturer} {self.model} ({self.registration_number})'

    def get_absolute_url(self):
        return reverse('car:car-detail', kwargs={'pk': self.pk})


class Mileage(models.Model):
    distance = models.PositiveSmallIntegerField(default=0)
    start_day_odometer = models.PositiveIntegerField(default=0)
    end_day_odometer = models.PositiveIntegerField(default=0)
    date = models.DateField(verbose_name='report date')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        ordering = ('car', '-end_day_odometer')

    # w formularzu nadpisac metodę save()
    def calculate_distance(self):
        return self.end_day_odometer - self.start_day_odometer

    def __str__(self):
        return f'{self.car.manufacturer} {self.car.model} {self.car.registration_number} on day {self.date}'
