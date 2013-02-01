# Create your views here
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def NewTextPost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			slug = slugify(title)
			text = form.cleaned_data['text']
			tags = form.cleaned_data['tags'].split()
			
			post = Post.objects.create(title=title,
									   slug=slug,
									   text=text,
									   tags=tags,)

			post.save()

			return HttpResponseRedirect('/dashboard/')

	

				

