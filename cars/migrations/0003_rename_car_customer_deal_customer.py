# Generated by Django 3.2.7 on 2021-09-15 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_customer_deal_car_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='car_customer',
            new_name='customer',
        ),
    ]