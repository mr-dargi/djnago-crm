from django import forms
from .models import Ticket, Message


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'description']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']