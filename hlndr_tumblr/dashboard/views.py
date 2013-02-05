# Create your views here.
from django.http import HttpResponseRedirect
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
		
