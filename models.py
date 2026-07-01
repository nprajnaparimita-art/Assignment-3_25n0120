from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Bounty(models.Model):
    STATUS_CHOICES = [
        ('wanted', 'Wanted'),
        ('captured', 'Captured'),
    ]

    target_name = models.CharField(max_length=100)
    reward = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.target_name