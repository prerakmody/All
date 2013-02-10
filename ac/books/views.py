# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import datetime
from django.db.models import Q
from models import *
from forms import ContactForm
#from forms import PublisherForm
from django.core.mail import send_mail



def search(request):
	query=request.GET.get('q','')
	if query:
		qset=(
			Q(title__icontains=query) |
			Q(authors__firstname__icontains=query) |
			Q(authors__lastname__icontains=query)
			)
		results=Book.objects.filter(qset).distinct()
	else:
		results=[]
	return render_to_response("books\\search.html",
		{"results":results,"query":query})

def contact(request):
	if request.method=='POST':
		form=ContactForm(request.POST)
		if(form.is_valid()):
			topic=form.cleaned_data['topic']
			message=form.cleaned_data['message']
			sender=form.cleaned_data.get('sender','noreply@example.com')
			#send_mail(
			#		'Fedback from your site,topic : %s' %topic,
			#		message,sender,
			#		['']
			#	)
			return HttpResponseRedirect('thanks.html')
	else:
		form=ContactForm()

	return render_to_response('books//contact.html',{'form':form})

def contact_thanks(request):
	sender=None
	if request.method=='POST':
		form=ContactForm(request.POST)
		if(form.is_valid()):
			sender=form.cleaned_data.get('sender','noreply@example.com')	
			t=get_template('books\\thanks.html')
			html=t.render(Context({'name':sender}))
	return HttpResponse(html)	


def add_publisher(request):
	if(request.method=='POST'):
		form=PublisherForm(request.POST)
		if(form.is_valid):
			form.save()
			return HttpResponseRedirect('th_publisheradd.html')
	else:
		form=PublisherForm()

	return render_to_response('books\\add_publisher.html',{'form':form})

def search_movies(request):
	request_params=request.GET.copy()
	fromdate=datetime.datetime.strptime(request_params['fromdate'])
	todate=datetime.datetime.strptime(request_params['todate'])
	film_results=Film.objects.filter(director__name=request_params['director'],
		created_at__range=(fromdate,todate))
	return render_to_response('search_movies.html',{'results':film_results})


