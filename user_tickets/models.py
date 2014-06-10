from django.db import models
from django.db.models import *
from django.contrib.auth.models import User
from django.contrib import admin
class Ticket(models.Model):
	user_id=models.EmailField(help_text="enter email")
	topic_id=models.CharField(max_length=100,help_text="enter topic id")
	message=models.TextField(help_text="enter message")
	ticket_id=models.IntegerField(help_text="enter tid")
	created_date_time=models.DateTimeField(auto_now_add=True)
	overdue_date_time=models.DateTimeField(auto_now_add=True)
	closed_date_time=models.DateTimeField(auto_now_add=True)
	status=models.IntegerField(help_text="enter status")
	reopened_date_time=models.DateTimeField(auto_now_add=True)
	topic_priority=models.IntegerField(help_text="enter priority")
	duration_for_reply=models.IntegerField(help_text="enter duration for reply")
        
        def __unicode__(self):
		return unicode(self.ticket_id)
