# Generated by Django 3.0.4 on 2020-03-08 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128)),
                ('street_number', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Customer name')),
                ('category', models.CharField(choices=[('SSO2', 'Self service shop over 2 checkouts'), ('SSU2', 'Self service shop under 2 checkouts'), ('CO', 'Counter shop')], default='CO', max_length=4, verbose_name='Customer category')),
                ('phone_number', models.PositiveSmallIntegerField()),
                ('nip', models.PositiveSmallIntegerField()),
                ('type', models.CharField(choices=[('WH', 'Wholesaler'), ('SH', 'Shop')], default='SH', max_length=2, verbose_name='Customer type')),
                ('is_active', models.BooleanField(default=True)),
                ('addresses', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerAddress')),
            ],
        ),
    ]
