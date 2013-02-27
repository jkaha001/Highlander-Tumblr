# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader, RequestContext
from django.utils import timezone
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#from users.forms import RegisterForm, LoginForm, ImageForm
from friends.models import Friendship

from utils.shortcuts import *

#function to fill friends page up with desired content
@login_required(login_url='/login/')
def friends_page(request, username):
	#get the user object from db but 404 if not there
	user = get_object_or_404(User, username=username)
	
	#get list of friends listed under the user
	friends = [friendship.to_friend for friendship in user.from_friend_set.all()]

	#get list of friends request issued by user
	fr_outgoing = user.invite_sender.all()

	#get list of friend request incoming to user
	fr_incoming = user.invite_reciever.all()

	#list of friends that should be shown (currently lists by recently added friends) [decending]
	recently_added_friends = [fs.to_friend for fs in user.from_friend_set.order_by('-friendSince')]

	variables = RequestContext(request, {
		'username': username,
		'friends': friends
		# could add these fields once sure about implementation
		#'top_friends': recently_added_friends[:10],
		#'show_tags': True,
		#'show_user': True
		})

	return render_to_response('friends_page.html', variables)

#function to actually add friends (should be a GET request)
@login_required(login_url='/login/')
def friend_add(request):
	#make sure the user is authenticated before performing action
	if request.user.is_authenticated(): 
		user = request.user
	
	#assuming there is a way to retrieve someones user info
	#it might be a button called "add friend" that issues a
	#a get request
	if 'username' in request.GET:
		#get the desired friends username
		friend = get_object_or_404(User, username=request.GET['username'])
		
		#make sure there was a friend request object
		fr = FriendRequest.objects.filter(sender=user, reciever=friend)
		if fr.count() == 0:
			raise Http404

		fr.accept();
		
		#make sure to redirect to the correct field
		return HttpResponseRedirect('/%s/friends/' % user.username)
	else: 
		raise Http404
	
'''def send_friend_request(request):
	#make sure the user is authenticated before performing action
	if request.user.is_authenticated(): 
		user = request.user
	
	if 'username' in request.GET:
		friend = get_object_or_404(User, username=request.GET['username'])

		friendRequest = FriendRequest(sender=user, reciever=friend)
		friendRequest.save()

		#not sure if stay on same page or redirect
		return HttpResponseRedirect('/')

	else:
		raise Http404'''
