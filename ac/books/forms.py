from django import forms 

TOPIC_CHOICES=(
	('general','General_Enquiry'),
	('bug','Bug report'),
	('suggestion','Suggestion')
	)

class ContactForm(forms.Form):
	topic=forms.ChoiceField(choices=TOPIC_CHOICES)
	message=forms.CharField(widget=forms.Textarea(),initial="replace with your Feedback")
	sender=forms.EmailField(required=False) 