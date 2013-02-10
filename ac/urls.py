from django.conf.urls.defaults import *
from ac import views
#from ac.views import hello,wtf,current_datetime,hours_ahead,temp1
#from ac.views import temp2,temp3,current_datetime2,current_datetime3
#from ac.books.views import search,contact,contact_thanks,add_publisher
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ac.views',
    ('^hello/$','hello'),
    ('^wtf/$','wtf'),
    (r'^time/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$','hours_ahead'),
    ('^temp1/$','temp1'),
    ('^temp2/$','temp2'),
    ('^temp3/$','temp3'),
    ('^time2/$','current_datetime2'),
    ('^time3/$','current_datetime3'),
    (r'^admin/$',include ('django.contrib.admindocs.urls'))
    )
   
urlpatterns+= patterns('ac.books.views',
     (r'^search/$','search'),(r'^contactus/$','contact'),
    (r'^contactus/thanks.html/$','contact_thanks'),
    (r'^add_publisher/$','add_publisher'),
    )
    # Example:
    # (r'^ac/', include('ac.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),

