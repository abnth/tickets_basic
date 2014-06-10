from django.shortcuts import render
from django import forms
from user_tickets.forms import SubmitTicketForm
from user_tickets.models import *
from user_tickets.forms import SubmitTicketForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from datetime import timedelta
from django.db.models import Max
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
def submit_ticket(request):
    if request.method=="POST":
        print request.POST
        submit_ticket_form=SubmitTicketForm(request.POST)
        if submit_ticket_form.is_valid():
            submit_ticket_form.save()
            print "success"
        else:
            print "form not valid"
    else:
        submit_ticket_form=SubmitTicketForm()
    return render_to_response(
    'user_tickets/submit_ticket.html',
    {'submit_ticket_form': submit_ticket_form},
    RequestContext(request))