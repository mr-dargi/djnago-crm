from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ticket, Message
from .forms import MessageForm
from .mixins import CreateFieldMixin, FormValidMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages


# Create your views here.
class Create_tickets(LoginRequiredMixin, CreateFieldMixin, FormValidMixin, CreateView):
  model = Ticket
  success_url = reverse_lazy("crm:home")
  template_name = "tickets/create_ticket.html"
  


@login_required
def ticket_details(request, ticket_id):
  ticket = get_object_or_404(Ticket, id=ticket_id)
  
  if request.method == "POST":
    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.save(commit=False)
      message.ticket = ticket
      message.sender = request.user
      message.save()
      return redirect('tickets:ticket_details', ticket_id=ticket_id)
  else:
    form = MessageForm()
  
  return render(request, "tickets/ticket_details.html", {"ticket": ticket, "form": form})


def delete_message(request, id):
    message = get_object_or_404(Message, pk=id)
    context = {'message': message}    
    
    if request.method == 'GET':
        return render(request, 'tickets/message_confirm_delete.html',context)
    elif request.method == 'POST':
        message.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('tickets:ticket_details', ticket_id=message.ticket.id)