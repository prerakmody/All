from django.db import models
from django import forms
from django.forms import ModelForm



class User(models.Model):
	name = models.CharField(max_length=30)
	rollno = models.IntegerField(max_length = 20)
	def __unicode__(self):
		return self.name

# Create your models here.
class Message(models.Model):
	from_user = models.ForeignKey(User,related_name="Message_from_user")
	to_user = models.ForeignKey(User,related_name="Message_to_user")
	content = models.TextField(max_length=1000)
	

class mod_form_user(forms.ModelForm):
	class Meta:
		model = User

class mod_form_msg(forms.ModelForm):
	class Meta:
		model = Message


class mod_getmsg(forms.ModelForm):
	class Meta:
		model = Message
		variables = ('from_user',)
