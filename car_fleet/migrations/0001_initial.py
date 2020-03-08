# Generated by Django 3.0.4 on 2020-03-07 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=7)),
                ('manufacture_year', models.PositiveSmallIntegerField()),
                ('engine_power', models.PositiveSmallIntegerField(help_text='Power is measured in horse power')),
                ('engine_size', models.PositiveSmallIntegerField(help_text='Size is measured in cm3')),
                ('odometer', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.PositiveSmallIntegerField(default=0)),
                ('start_day_odometer', models.PositiveIntegerField(default=0)),
                ('end_day_odometer', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(verbose_name='report_date')),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_fleet.Car')),
            ],
        ),
    ]