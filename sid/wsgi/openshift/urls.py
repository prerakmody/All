from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('openshift.views',
    # Examples:
     (r'^$','home'),
     (r'^AlumniForm$', 'AlumniForm'),
     (r'^AlumniForm/redirect_reg/$','AlumniForm'),
     (r'^profile$', 'profilePage'),



    # url(r'^AlumniConnect/', include('AlumniConnect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns+=patterns('openshift.views',
    (r'^SendMessage/$','SendMessage'),
    (r'^DisplayMessages/$','DisplayMessages'),
    (r'^GetMessage/$','GetMessage'),
    (r'^DisplayUsers$','DisplayUsers'),
    )
