# Generated by Django 3.0.4 on 2020-03-08 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200308_1358'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='package',
            unique_together={('type', 'capacity', 'capacity_type', 'multipack_quantity')},
        ),
    ]