from django.conf.urls import patterns, include, url
from one.oneTest.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^AlumniForm$',AlumniForm),
    # Examples:
    # url(r'^$', 'one.views.home', name='home'),
    # url(r'^one/', include('one.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
