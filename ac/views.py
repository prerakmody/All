from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("hellow World")
def wtf(request):
	return HttpResponse("WTF!!")
def current_datetime(request):
	now=datetime.datetime.now()
	t=Template("<html><body>It is now {{current_date}}.</body></html>")
	html=t.render(Context({'current_date':now}))
	return HttpResponse(html)
def current_datetime2(request):
	now=datetime.datetime.now()
	t=get_template('current_datetime.html')
	html=t.render(Context({'current_datetime':now}))
	return HttpResponse(html)
def current_datetime3(request):
	now=datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_datetime':now})
def hours_ahead(request,offset):
	#offset=int(offset)
	dt= datetime.datetime.now() + datetime.timedelta(hours=offset)
	html="<html><body>In %s hour(s), it will be %s</body></html>" %(offset,dt)
	return HttpResponse(html)
def temp1(request):
	person={'name':'Sally','age':'43'}
	t=Template('{{person.name}} is {{person.age}} years old')
	c=Context({'person':person})
	return HttpResponse(t.render(c))
class Person(object):
	
	def __init__(self,first_name,last_name):
		self.first_name,self.last_name=first_name,last_name
def temp2(request):
	t=Template('Hello, {{person.first_name}} {{person.last_name}}.')
	c=Context({'person':Person('Prerak','Mody')})
	return HttpResponse(t.render(c))
def temp3(request):
	t=Template('Item 2 in the list is {{items.2}}.')
	c=Context({'items:("apples","bananas","carrots")'})
	return HttpResponse(t.render(c))


