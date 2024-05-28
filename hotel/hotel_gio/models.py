from django.db import models


# Create your models here.

# models.py
from django.db import models

class Booking(models.Model):
    room_type = models.CharField(max_length=200)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()

