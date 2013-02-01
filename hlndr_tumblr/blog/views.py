# Create your views here
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import Post
from blog.forms import PostForm

def home(request,username):
	author = get_object_or_404(User,username=username)
	posts = author.post_set.all().order_by('-post_date')
	return render_to_response('blog/home.html',
							  {'author':author,
							   'posts':posts,},
							   context_instance=RequestContext(request))

@login_required(login_url='/login/')
def NewTextPost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			slug = slugify(title)
			text = form.cleaned_data['text']
			
			post = Post.objects.create(title=title,
									   slug=slug,
									   text=text,
									   author=request.user,)

			return HttpResponseRedirect('/dashboard/')
		else:
			return render_to_response('blog/textpost.html',
									  {'form':form,
									   'invalid': "Missing some required fields"},
									  context_instance=RequestContext(request))
	
	return render_to_response('blog/textpost.html',
							  context_instance=RequestContext(request))

