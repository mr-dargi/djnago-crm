from django.db import models
from django.urls import reverse
from account.models import User
from extensions.utils import jalali_converter


# Create your models here.
class Project_procedure(models.Model):
  # customer -> customer model is foreignkey from User tabel
  user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="کاربر")
  support = models.ForeignKey(User, null=True, related_name="supports", on_delete=models.SET_NULL, verbose_name="پشتیبانی")
  
  # genrals for time
  created = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  
  # ------------------------------ Description of project procedure model actor customer ------------------------------ #
  # rfp -> rfp model is for rfp that's writed by customer the project they want as pdf we will receive it and save it in media/rfps
  # confirm_proposal -> confirm_proposal model it's boolean field, that will use it when the support saw the rfp and will send explanation of project and invoice to customer and customer can accept or reject the proposal
  # description_reject_proposal -> description_reject_proposal model, when the customer reject the proposal and we want to know why company/he/she rejected
  # contract_image -> contract_image model, when the support send contract to customer after the sign and fill contract it will be receive it as image
  # payment_receipt_image -> payment_receipt_image model, when the support send payment of project to the customer after pay of, it will send image of payment receipt
  # confirm_design -> confirm_design model it's boolean field, that will use it for confirm or reject of design
  # description_reject_design -> description_reject_design model, when the customer reject design could describe why company/he/she didn't like the disgn
  
  # ---------------------------------------- stage 1 -------------------------------------------------------------------- #
  project_title = models.CharField(max_length=200, default='پروژه جدید', verbose_name = "عنوان پروژه")
  rfp = models.FileField(upload_to="uploads/rfps", blank=True, null=True, verbose_name="آر اف پی")
  # ---------------------------------------- stage 2 -------------------------------------------------------------------- #
  confirm_proposal = models.BooleanField(default=False, verbose_name = "وضعیت پروپوزال")
  description_reject_proposal = models.TextField(blank=True, null=True, verbose_name = "دلیل رد کردن پروپوزال")
  # ---------------------------------------- stage 3 -------------------------------------------------------------------- #
  contract_image = models.ImageField(upload_to="images/contract", blank=True, null=True, verbose_name = "ارسال اسکن قرارداد")
  # ---------------------------------------- stage 4 -------------------------------------------------------------------- #
  payment_receipt_image = models.ImageField(upload_to="images/payment", blank=True, null=True, verbose_name = "رسید پرداخت")
  # ---------------------------------------- stage 5 -------------------------------------------------------------------- #
  confirm_design = models.BooleanField(default=False, verbose_name = "وضعیت طراحی")
  description_reject_design = models.TextField(blank=True, null=True, verbose_name = "دلیل رد کردن طراحی")
  # timer_for_satisfaction = models.DateTimeField(default=timezone.now, verbose_name = "زمان پرسش سوال رضایتمندی از پروژه")
  # ask_for_satisfaction = models.BooleanField(default=True, verbose_name = "وضعیت رضایتمندی")
  # description_of_dissatisfaction = models.TextField(blank=True, null=True, verbose_name = "دلیل رد کردن طراحی")
  
  # ------------------------------ Description of project procedure model actor support ------------------------------ #
  # proposal -> proposal model is write dowm by support about project and invoice of project and it will send it to customer for comfirm or reject
  # contract -> contract model is pdf that support will send to customer to fill it up by customer and it will send it to support
  # payment -> payment model is pdf that support will send it to customer and customer should pay it for Continuation of the project
  # confirm_contract  -> confirm_contract model is for after sending contract by customer to support, and support will confirm or reject correctness of contract
  # description_reject_contract -> description_reject_contract model is for the time when support will reject the correctness of contract and support will explain why this contract rejected
  # confirm_payment_receipt -> confirm_payment_receipt model is for after send the payment support and customer will send payment receipt duty of support is confirm or reject the payment receipt
  # description_reject_payment_receipt -> description_reject_payment_receipt model is for the time when support will reject the correctness of payment receipt and support will explain why this payment receipt rejected
  
  # ---------------------------------------- stage 6 -------------------------------------------------------------------- #
  proposal = models.FileField(upload_to="uploads/proposals", blank=True, null=True, verbose_name="پروپوزال")
  # ---------------------------------------- stage 7 -------------------------------------------------------------------- #
  contract = models.FileField(upload_to="uploads/contract", blank=True, null=True, verbose_name="قرارداد")
  confirm_contract = models.BooleanField(default=False, verbose_name = "وضعیت قرارداد")
  description_reject_contract = models.TextField(blank=True, null=True, verbose_name = "دلیل رد کردن قرارداد")
  # ---------------------------------------- stage 8 -------------------------------------------------------------------- #
  payment = models.FileField(upload_to="uploads/payment", blank=True, null=True, verbose_name="صورت حساب")
  confirm_payment_receipt = models.BooleanField(default=False, verbose_name = "وضعیت رسید پرداخت")
  description_reject_payment_receipt = models.TextField(blank=True, null=True, verbose_name = "دلیل رد کردن رسید پرداخت")
  
  class Meta:
    verbose_name = "روند پروژه"
    verbose_name_plural = "روند پروژه ها"
    ordering = ["-created"]
    
  def __str__(self):
    return self.project_title
  
    
  def get_absolute_url(self):
    return reverse("account:home")
  
  def jcreate(self):
    return jalali_converter(self.created)
  
  jcreate.short_description = "زمان ثبت اولیه پروژه"