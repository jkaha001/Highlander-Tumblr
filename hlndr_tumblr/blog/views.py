# Create your views here
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

from blog.models import Post, PhotoPost
from blog.forms import PostForm, PhotoForm

def home(request,username):
	author = get_object_or_404(User,username=username)
	posts = list(author.post_set.all())
	posts += list(author.photopost_set.all())

	# sort from oldest to newest, then reverse to get latest
	posts = reversed(sorted(posts, key=lambda post: post.post_date))
	return render_to_response('blog/home.html',
							  {'author':author,
							   'posts':posts,},
							   context_instance=RequestContext(request))

@login_required(login_url='/login/')
def new_text_post(request):
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

@login_required(login_url='login')
def new_photo_post(request):
	invalid = ""
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES['photo']
			caption = form.cleaned_data['caption']
			post = PhotoPost.objects.create(filename=file.name,
											url="",
											caption=caption,
											author=request.user)

			filepath = "%s/image/%s/%s" % (request.user.username, str(post.id), file.name)
			upload_to_s3(file, filepath)
			post.url = "http://d1852nuusu2e8n.cloudfront.net/" + filepath
			post.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No Photo Selected"
	else:
		form = PhotoForm()
	return render_to_response('blog/photopost.html',
							  {'form':form,
							   'invalid':invalid},
							  context_instance=RequestContext(request))

def upload_to_s3(file, filepath):
	destination = default_storage.open(filepath, 'wb+')
	for chunk in file.chunks():
		destination.write(chunk)
	destination.close()
