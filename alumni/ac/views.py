from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q
from ac.models import *
#from ac.models import mod_form_alumni,mod_form_faculty

def reg_form_alumni(request):
	if(request.method == 'POST'):
		form=mod_form_alumni(request.POST)
		if (form.is_valid()):
			form.save()
			return HttpResponseRedirect('thanks.html')
	else:
		form=mod_form_alumni()
	#variables=RequestContext(request,{'form':form})
	return render_to_response('reg_form_alumni.html',{'form':form})

def search(request):
	query=request.GET.get('batch','stream','city')
	if query:
		qset=(
			Q(title__icontains=query) |
			Q(authors__firstname__icontains=query) |
			Q(authors__lastname__icontains=query)
			)
		results=alumni.objects.filter(qset).distinct()
	else:
		results=[]
	return render_to_response("search.html",
		{"results":results,"query":query})