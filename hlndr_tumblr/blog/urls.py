from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^text/$', 'blog.views.NewTextPost', name='newtext'),
)
