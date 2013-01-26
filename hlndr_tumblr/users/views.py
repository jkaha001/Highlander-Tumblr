# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader, RequestContext
from django import forms
from django.utils import timezone
from django.shortcuts import get_object_or_404
from users.models import User
from users.forms import RegisterForm, LoginForm


# user homepage
def home(request, username):
	user = get_object_or_404(User, username=username)
	template = loader.get_template('users/home.html')
	context = Context({
		'username': user.username,
	})
	return HttpResponse(template.render(context))

# login page
def login(request):

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
		
			# hacky 404 will change	
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				raise Http404

			if password == user.password:
				return HttpResponseRedirect('/' + user.username + '/')	

	template = loader.get_template('users/login.html')
	context = RequestContext(request)
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
	

	
