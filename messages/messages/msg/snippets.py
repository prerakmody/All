#CODE SNIPPETS
#####################################################################
from django.http import HttpResponse
def my_image(request):
    image_data = open("/path/to/my/image.png", "rb").read()
    return HttpResponse(image_data, mimetype="image/png")

#####################################################################
from django.http import HttpresponseRedirect
urlpatterns=patterns('',
	(r'^some_url$',lambda x:HttpresponseRedirect('/someurl or view.py def')))


#####################################################################