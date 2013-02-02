from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^text/$', 'blog.views.new_text_post', name='newtext'),
	url(r'^photo/$', 'blog.views.new_photo_post', name='newtext'),
)
