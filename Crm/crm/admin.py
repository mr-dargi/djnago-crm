from django.contrib import admin
from .models import Project_procedure

# Register your models here.
class ProjectProcedureAdmin(admin.ModelAdmin):
  # Add Project_procedure model to admin panel
  list_display = (
    "user",
    "project_title",
    "rfp",
    "confirm_proposal",
    "description_reject_proposal",
    "contract_image",
    "payment_receipt_image",
    "confirm_design",
    "description_reject_design",
    "proposal",
    "contract",
    "payment",
    "confirm_contract",
    "description_reject_contract",
    "confirm_payment_receipt",
    "description_reject_payment_receipt",
  )

admin.site.register(Project_procedure, ProjectProcedureAdmin)