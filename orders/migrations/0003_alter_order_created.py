# Generated by Django 5.0.7 on 2024-12-17 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(default=datetime.date(2024, 12, 17)),
        ),
    ]
