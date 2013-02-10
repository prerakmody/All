from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('alumni.ac.views',
	(r'^reg_alumni/$','reg_form_alumni'),
    # Example:reg_form_alumni
    # (r'^alumni/', include('alumni.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^debuginfo$', 'alumni.ac.views.debug'),
        (r'^debuginfo$', 'alumni.views.debug'),
    )