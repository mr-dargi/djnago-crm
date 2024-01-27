from django.urls import path
from .views import Create_tickets, ticket_details, delete_message


app_name = "tickets"
urlpatterns = [
    path('create_ticket/', Create_tickets.as_view(), name='create_ticket'),
    path('ticket_details/<int:ticket_id>/', ticket_details, name='ticket_details'),
    path('delete/<int:id>/', delete_message, name='delete_message'),
]