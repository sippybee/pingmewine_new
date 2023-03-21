from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Deal(models.Model):
    pass


class Phonenumber(models.Model):
    phone_number = PhoneNumberField()
    entry = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.phone_number}, {self.created}"