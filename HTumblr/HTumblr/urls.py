from django.conf.urls import patterns, include, url
from HTumblr.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HTumblr.views.home', name='home'),
    # url(r'^HTumblr/', include('HTumblr.HTumblr.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Enable homepage
    (r'^$', main_page),

    #Enables auth forms
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),

    #Enables user dashboard
    url(r'^dashboard/', include('HTumblr.dashboard.urls')),

    #Serve static content.
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': 'static'}),

    #Registration forms
    #(r'^admin/', include('django.contrib.admin.urls')),
    (r'^accounts/', include('HTumblr.registration.urls')),
)
