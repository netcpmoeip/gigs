# Generated by Django 5.0.7 on 2024-10-11 11:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid', max_length=20)),
                ('created', models.DateField(default=datetime.date(2024, 10, 11))),
                ('total', models.PositiveIntegerField(default=0, null=True)),
                ('places', models.PositiveIntegerField(default=0, null=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('leg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.leg')),
            ],
        ),
    ]