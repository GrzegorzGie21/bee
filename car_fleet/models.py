from django.db import models
from django.contrib.auth.models import User


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

    def get_odometer(self):
        mileage = Mileage.objects.filter(car_id=self.pk).order_by('-date').first()
        return mileage.end_day_odometer

    def __str__(self):
        return f'{self.manufacturer} {self.model}: {self.registration_number}'


class Mileage(models.Model):
    distance = models.PositiveSmallIntegerField(default=0)
    start_day_odometer = models.PositiveIntegerField(default=0)
    end_day_odometer = models.PositiveIntegerField(default=0)
    date = models.DateField(verbose_name='report_date')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    # w formularzu nadpisac metodę save()
    def calculate_distance(self):
        return self.end_day_odometer - self.start_day_odometer

    def __str__(self):
        return f'Car: {self.car.registration_number} on day {self.date}'
