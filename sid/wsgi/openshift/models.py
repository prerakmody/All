from django.db import models
from django import forms
from django.forms import ModelForm
from datetime import date
from datetime import datetime

current_year = datetime.now().year
def tuplify(x):return (x,x)
YEARS = map(tuplify,range(1930, current_year + 1))
BRANCH=map(tuplify,('B.TECH ECE','B.TECH CSE' ))
#models
class User(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    #dob = models.DateField()
    batch=models.IntegerField(choices=YEARS)
    branch = models.CharField(max_length=10,choices=BRANCH)
    email = models.EmailField()
    #headshot = models.ImageField(upload_to='/profilepictures')
    #created = models.DateTimeField(db_index=True, auto_now_add=True)
    #modified=models.DateTimeField(auto_now=True)

    def __unicode__(self):
    	name = self.first_name + " " + self.last_name
    	return name


class Message(models.Model):
	from_id = models.ForeignKey(User, related_name="from_id")
	to_id = models.ForeignKey(User, related_name="to_id")
	content = models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)

#forms
class alumniForm(forms.ModelForm):
	class Meta:
		model = User
		variables={'first_name',}

class messageForm(forms.ModelForm):
	class Meta:
		model = Message


class getMessage(forms.ModelForm):
	class Meta:
		model = Message
		variables = ('from_id',)
		


#fundamentals



class OpenPrivacy(models.Model):
	UserID1 = models.ForeignKey(User, related_name = "Request_from_user")
	UserID2 = models.ForeignKey(User, related_name = "Request_to_user")
	requestStatus = models.BooleanField()
	'''
	requestStatus:
		if true: means accepted
		if false: means waiting
		if a model like this does not exist : that means no request has been sent yet.
	'''




	
	

		
		
	


	
		
		
		