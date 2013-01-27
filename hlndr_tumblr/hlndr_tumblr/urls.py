from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hlndr_tumblr.views.home', name='home'),
    # url(r'^hlndr_tumblr/', include('hlndr_tumblr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	# home page 
	url(r'^$', 'hlndr_tumblr.views.home', name='home'),
	url(r'^register/$', 'users.views.register', name='register'),
	url(r'^login/$', 'users.views.log_in', name='log_in'),
	url(r'^logout/$', 'users.views.log_out', name='log_out'),
	url(r'^dashboard/$', 'dashboard.views.dashboard', name='dashboard'),
	url(r'^(?P<username>\w+)/$', 'users.views.home', name='users.home')

)
