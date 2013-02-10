from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from openshift.models import *
from django.views.decorators.csrf import csrf_exempt

#Static pages
@csrf_exempt
def home(request):
	return HttpResponse("Alumni Connect framework\n\nUnder Contruction as on 04/02/2013")

#Dynamic Pages / Forms / Pages which need arguments
@csrf_exempt	
def profilePage(request):
	if request.method == "GET":
		userID = str(request.GET['id'])
		results = User.objects.filter(id=userID)
		userName = "did you enter a valid ID?"
		for x in results:
			userName = x
		if results:
			return render_to_response("profile.html", )
		else:
			return HttpResponse("not found user")
			#Point to the standard 404 page

#Data Acceptor
@csrf_exempt
def AlumniForm(request):
	if(request.method=='POST'):
		form = alumniForm(request.POST)
		if(form.is_valid()):
			form.save()
			message = "Success!"
			form_t = alumniForm()
			return render_to_response("reg_form_alumni.html",{'form':form_t,'msg':message})
	else :
		  form = alumniForm()

	return render_to_response("reg_form_alumni.html",{'form':form})


@csrf_exempt
def SendMessage(request):
	if(request.method=='POST'):
		form = messageForm(request.POST)
		if(form.is_valid()):
			form.save()
			message = "Success!"
			form_t = messageForm()
			return render_to_response("send_message.html",{'form':form_t,'msg':message})
	else :
		  form = messageForm()
	return render_to_response("send_message.html",{'form':form})

def DisplayMessages(request):
	messages = Message.objects.all()
	return render_to_response('DisplayMessages',{'lists':messages})
	
def GetMessage(request):
	lists={}
	if(request.method=='POST'):
		form = getMessage(request.POST)
		if(form.is_valid()):
			form.save()
	else :
		  form = getMessage()

	return HttpResponseRedirect(SearchMessages(request,form))

def SearchMessages(request,form):
	request_params=request.GET.copy()
	#fromdate=datetime.datetime.strptime(request_params['fromdate'])
	#todate=datetime.datetime.strptime(request_params['todate'])
	#film_results=Film.objects.filter(director__name=request_params['director'],
	#		created_at__range=(fromdate,todate))
	#return render_to_response('search_movies.html',{'results':film_results})

def DisplayUsers(request):
    lists=User.objects.all()
    return render_to_response('display_users.html',{'lists':lists})

		





