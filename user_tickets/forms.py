from user_tickets.models import *
from django import forms
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
class SubmitTicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=('user_id','topic_id','message','ticket_id','status','topic_priority','topic_priority','duration_for_reply')
        #'created_date_time','overdue_date_time','closed_date_time','reopened_date_time',