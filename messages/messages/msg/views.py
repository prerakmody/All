# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from messages.msg.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def reg_form_alumni(request):
	if(request.method=='POST'):
		form = mod_form_user(request.POST)
		if(form.is_valid()):
			form.save()
			message = "Success!"
			form_t = mod_form_user()
			return render_to_response("reg_form_alumni.html",{'form':form_t,'msg':message})
	else :
		  form = mod_form_user()

	return render_to_response("reg_form_alumni.html",{'form':form})

@csrf_exempt
def send_message(request):
	if(request.method=='POST'):
		form = mod_form_msg(request.POST)
		if(form.is_valid()):
			form.save()
			message = "Success!"
			form_t = mod_form_msg()
			return render_to_response("send_message.html",{'form':form_t,'msg':message})
	else :
		  form = mod_form_msg()

	return render_to_response("send_message.html",{'form':form})

def display_messages(request):
	messages = Message.objects.all()
	return render_to_response('data.html',{'lists':messages})
	
def getmsg(request):
	lists={}
	if(request.method=='POST'):
		form = mod_getmsg(request.POST)
		if(form.is_valid()):
			form.save()
			lists=Message.object.filter(User__from_user='vidit')
	else :
		  form = mod_form_msg()

	return render_to_response("data.html",{'lists':lists})

def display_users(request):
	lists=User.objects.all()
	return render_to_response('display_users.html',{'lists':lists})



 