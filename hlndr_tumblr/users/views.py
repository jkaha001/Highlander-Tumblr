# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader, RequestContext
from django.utils import timezone
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# from users.models import User
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
def log_in(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/dashboard/')
				else:
					return render_to_response('users/login.html',
											  {'form':form,
											   'invalid':"Account disabled"},
											  context_instace=RequestContext(request))
			else:
				return render_to_response('users/login.html',
										  {'form':form,
										   'invalid':"Invalid username or password"},
										  context_instance=RequestContext(request))

	template = loader.get_template('users/login.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')

# registration page
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			
			# Validate fields
			if form.cleaned_data['password1'] == form.cleaned_data['password2']:
				password = form.cleaned_data['password1']
			else:
				return render_to_response('users/register.html',
										  {'form':form,
										   'invalid':"Passwords mismatched"},
										   context_instance=RequestContext(request))

			username = form.cleaned_data['username']
			email = form.cleaned_data['email']	
			newuser = User(username=username,email=email)
			newuser.set_password(password)
			newuser.creation_date = timezone.now()
			newuser.save()

			return HttpResponseRedirect('/' + newuser.username + '/')
		
		else:
			return render_to_response('users/register.html',
									  {'form':form,
									   'invalid':"All fields required"},
									  context_instance=RequestContext(request))
	else:
		form = RegisterForm()

	return render_to_response('users/register.html',
							  context_instance=RequestContext(request))	
