# Generated by Django 3.0.4 on 2020-03-08 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200308_1333'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'net_price', 'vat', 'have_promotion', 'packages')},
        ),
    ]
