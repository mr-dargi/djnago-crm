from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Ticket, Message
from .forms import TicketForm, MessageForm

# Create your views here.
@login_required
def create_ticket(request):
  if request.user.is_customer or request.user.is_superuser:
    if request.method == "POST":
      form = TicketForm(request.POST)
      if form.is_valid():
        ticket = form.save(commit=False)
        ticket.customer = request.user
        ticket.save()
        return redirect("ticket_details", ticket_id=ticket.id)
    else:
      form = TicketForm()
  
    return render(request, "tickets/create_ticket.html", {"form": form})
  else:
      raise Http404("You can't access this page.")


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
      return redirect("ticket_details", ticket_id=ticket.id)
  else:
    form = MessageForm()
  
  return render(request, "tickets/ticket_details.html", {"ticket": ticket, "form": form})