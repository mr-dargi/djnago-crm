from django import forms
from customer.models import Customer
from account.models import User


class CustomerProfileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    
    super(CustomerProfileForm, self).__init__(*args, **kwargs)
    
  class Meta:
      model = Customer
      fields = ["brand_name","adress","province","city"]


class SupportProfileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop("user")
    
    super(SupportProfileForm, self).__init__(*args, **kwargs)
    
    self.fields["username"].help_text = None
    
    if not user.is_superuser:
      self.fields["username"].disabled = True
      self.fields["email"].disabled = True
      self.fields["is_manager"].disabled = True
      self.fields["is_customer"].disabled = True
    
  class Meta:
      model = User
      fields = ["username","email","first_name","last_name","is_manager","is_customer"]