from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from .states import STATES

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True)
    sub_id = models.CharField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.username}, {self.created}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=400, blank=True)
    street_one = models.CharField(max_length=200, blank=False)
    street_two = models.CharField(max_length=200, blank=True)
    city  = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=20, choices=STATES, default='alaska')
    zip_code = models.CharField(max_length=10, blank=False)
    bio = models.TextField(blank=True, max_length=500)
    city = models.CharField(max_length=200, blank=True)
    collecting = models.BooleanField(default=True)
    gooddeals = models.BooleanField(default=True)
    justforfun = models.BooleanField(default=True)
    image = models.ImageField(upload_to='account')

    def __str__(self):
        return str(self.use.username)
