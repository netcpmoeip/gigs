# Generated by Django 5.0.7 on 2024-10-12 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(default=datetime.date(2024, 10, 12)),
        ),
    ]