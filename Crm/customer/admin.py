from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  # Add Customer model to admin panel
  list_display = (
    "customer",
    "brand_name",
    "adress",
    "province",
    "city",
  )

admin.site.register(Customer, CustomerAdmin)