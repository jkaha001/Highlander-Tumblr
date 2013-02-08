# Create your views here.
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from blog.views import get_post_list_by_author, delete_post

@login_required(login_url='/login/')
def dashboard(request):
	if request.user.is_authenticated():
		user = request.user

	return render_to_response('dashboard/dashboard.html',
							  context_instance=RequestContext(request))

def sort_posts_by_oldest(posts):
	posts = sorted(posts, key=lambda post: post.post_date)
	return posts

def sort_posts_by_newest(posts):
	posts = reversed(sorted(posts, key=lambda post: post.post_date))
	return posts

@login_required(login_url='/login/')
def deletepost(request, post_type, post_id):
	posts = get_post_list_by_author(request.user)
	for post in posts:
		if post.classname().lower() == post_type:
			if post.id == int(post_id):
				delete_post(post)
				return HttpResponseRedirect('/' + request.user.username + '/posts/')
	raise Http404

@login_required(login_url='/login/')
def viewposts(request, username):
	posts = get_post_list_by_author(request.user)
	
	#posts = sort_posts_by_newest(posts)
	#posts = sort_posts_by_oldest(posts)
	posts = sort_posts_by_newest(posts)		
	
	return render_to_response('dashboard/viewposts.html',
							  {'posts':posts, 'user':request.user},
							  context_instance=RequestContext(request))			
