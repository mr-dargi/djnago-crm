from django import forms
from customer.models import Customer


class ProfileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    # user = kwargs.pop("user")
    
    super(ProfileForm, self).__init__(*args, **kwargs)
    
  class Meta:
      model = Customer
      fields = ["brand_name","adress","province","city"]