# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django import forms
from django.utils import timezone
from django.shortcuts import get_object_or_404
from users.models import User
from users.forms import RegisterForm


# user homepage
def home(request, username):
	user = get_object_or_404(User, username=username)
	template = loader.get_template('users/home.html')
	context = Context({
		'username': user.username,
	})
	return HttpResponse(template.render(context))

# registration page
def register(request):

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			regUsername = form.cleaned_data['registerUsername']
			regPassword = form.cleaned_data['registerPassword']
			regEmail = form.cleaned_data['registerEmail']
			
			newuser = User(username=regUsername,password=regPassword,email=regEmail)
			newuser.creation_date = timezone.now()

			newuser.save()

			return HttpResponseRedirect('/' + newuser.username + '/')	

	template = loader.get_template('users/register.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))
	

	
