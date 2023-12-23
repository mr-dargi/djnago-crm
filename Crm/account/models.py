from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Add extra detail of user email and phone and also the status of user in website
class User(AbstractUser):
  # ------------------------------ Add fields to our User model ------------------------------ #
  # phone -> phone model is receive phone number of user
  # is_manager -> is_manager model is for determine of user state as manager
  # is_customer -> is_customer model is for determine of user state as customer
  phone = PhoneField(blank=False, verbose_name="شماره تلفن")
  is_manager = models.BooleanField(default=False, verbose_name="ادمین")
  is_customer = models.BooleanField(default=True, verbose_name = "کاربر عادی")