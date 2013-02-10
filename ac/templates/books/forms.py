from django import forms
from models import Publisher
from django.newforms import form_for_model

TOPIC_CHOICES=(
	('general','General_Enquiry'),
	('bug','Bug report'),
	('suggestion','Suggestion')
	)

class ContactForm(forms.Form):
	topic=forms.ChoiceField(choices=TOPIC_CHOICES)
	message=forms.CharField(widget=forms.TextArea())
	sender=froms.EmailField(required=False) 
	def clean_message(self):
		message=self.cleaned_data.get('message','')
		num_words=len(message.split())
		if (num_words < 4):
			raise forms.validationError("Not enough Words")
		return message

PublisherForm=form_for_model(Publisher)