from django.db import models
from django.forms import ModelForm
from django import forms

class user(models.Model):
	name = models.CharField(max_length=30)
	rollno = models.IntegerField(max_length = 20)
	def __unicode__(self):
		return self.name

class alumni(models.Model):
	batch=models.CharField(max_length=30)
	basic=models.ForeignKey(user)
    

class alumniForm(forms.ModelForm):
	class Meta:
		model = user

# Create your models here.
