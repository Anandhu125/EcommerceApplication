# Generated by Django 4.0.5 on 2023-02-08 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=260, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2023, 2, 13)),
        ),
    ]
