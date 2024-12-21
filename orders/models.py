from django.db import models
from datetime import datetime, date

# Create your models here.
class Order(models.Model):
    STATUS = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid')
    ]
    status = models.CharField(max_length=20, choices=STATUS, default='unpaid')
    created = models.DateField(default=datetime.now().date())
    total = models.PositiveIntegerField(null=True, default=0)
    leg = models.ForeignKey('main.Leg', on_delete=models.PROTECT, null=True)
    places = models.PositiveIntegerField(null=True, default=0)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)