from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from users.models import UserProfile
from blog.views import get_post_list_by_author, delete_post

@login_required(login_url='/login/')
def following(request):
	if request.user.is_authenticated():
		user = request.user
	myself = get_object_or_404(User, username=user.username)
	myprofile = get_object_or_404(UserProfile, user=myself)
	followlist = myprofile.following.all()
	return render_to_response('following/following.html',
							  {'follower_list':followlist, 'count':followlist.count()},
							  context_instance=RequestContext(request))

@login_required(login_url='/login/')
def follow(request, username):
    if request.user.is_authenticated():
        user = request.user.username
    
    #following
    myself = get_object_or_404(User, username=request.user.username)
    myprofile = get_object_or_404(UserProfile, user=myself)

    other = get_object_or_404(User, username=username)
    otherprofile = get_object_or_404(UserProfile, user=other)
    if myprofile != otherprofile:
        myprofile.following.add(otherprofile)
        myprofile.save()

    return render_to_response('following/following.html', {'follower_list':myprofile.following.all()}, context_instance=RequestContext(request))

