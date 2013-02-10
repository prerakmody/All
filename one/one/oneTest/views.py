# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from one.oneTest.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def AlumniForm(request,):
	if(request.method=='POST'):
		form = alumniForm(request.POST)
		if(form.is_valid()):
			form.save()
			message = "Success!"
			form_t = alumniForm()
			return render_to_response("AlumniForm.html",{'form':form_t,'msg':message})
	else :
		  form = alumniForm()

	return render_to_response("AlumniForm.html",{'form':form})