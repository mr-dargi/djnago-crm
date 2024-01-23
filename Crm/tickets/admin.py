from django.contrib import admin
from .models import Ticket, Message


class TicketAdmin(admin.ModelAdmin):
  # Add Ticket model to admin panel
  list_display = (
    "customer",
    "support",
    "subject",
    "description",
    "created_at",
    "updated_at",
  )

admin.site.register(Ticket, TicketAdmin)


class MessageAdmin(admin.ModelAdmin):
  # Add Project_procedure model to admin panel
  list_display = (
    "ticket",
    "sender",
    "content",
    "created_at",
  )

admin.site.register(Message, MessageAdmin)