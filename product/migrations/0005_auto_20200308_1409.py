# Generated by Django 3.0.4 on 2020-03-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200308_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=1.0, help_text='Describe promotion value i.e. 1 means no promotion, 0.95 means 5% discount', max_digits=3),
        ),
    ]
