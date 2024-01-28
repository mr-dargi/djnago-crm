from django.db import models
from account.models import User
from extensions.utils import jalali_converter


class Ticket(models.Model):
  customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="مشتری")
  support = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tickets', blank=True, null=True, verbose_name="ساپورت")
  subject = models.CharField(max_length=200, verbose_name="موضوع")
  description = models.TextField(verbose_name="توضیحات")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ارسال")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="زمان ویرایش")
  
  class Meta:
    verbose_name = "تیکت"
    verbose_name_plural = "تیکت ها"
    ordering = ["-created_at"]


class Message(models.Model):
  ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="messages", verbose_name="تیکت")
  sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ارسال کننده")
  content = models.TextField(verbose_name="محتوا")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ارسال")
  
  class Meta:
    verbose_name = "پیام"
    verbose_name_plural = "پیام ها"
    ordering = ["-created_at"]
  
  def message_jcreate(self):
    return jalali_converter(self.created_at)
  
  message_jcreate.short_description = "زمان ثبت ارسال پیام"