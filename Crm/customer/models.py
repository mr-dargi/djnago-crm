from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.
class Customer(models.Model):
  # customer -> customer model is foreignkey from User tabel
  customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="مشتری")
  
  # ------------------------------ Description of customer model ------------------------------ #
  # brand_name -> brand_name model is for customer who have company and in brand_name he/she will put their name of the company
  # adress -> adress model is customer address
  # province -> province model is province that customer company/home address is blong to
  # city -> city model is city that customer company/home address is blong to
  brand_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="نام تجاری")
  adress = models.CharField(max_length=200, blank=True, null=True, verbose_name="آدرس")
  province = models.CharField(max_length=50, blank=True, null=True, verbose_name="استان")
  city = models.CharField(max_length=50, blank=True, null=True, verbose_name="شهر")
  
  def __str__(self):
    return self.customer.get_full_name()
  
  class Meta:
    verbose_name = "مشتری"
    verbose_name_plural = "مشتری ها"