# Create your views here
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

from blog.models import TextPost, PhotoPost, VideoPost, AudioPost
from blog.forms import TextForm, PhotoForm, VideoForm, AudioForm

amazon_url = "https://s3-us-west-1.amazonaws.com/highlander-tumblr-test-bucket/"

# Upload to s3 using filepath starting from bucket root
def upload_to_s3(file, filepath):
	destination = default_storage.open(filepath, 'wb+')
	for chunk in file.chunks():
		destination.write(chunk)
	destination.close()

# Delete from s3 using filepath starting from bucket root
def delete_from_s3(filepath):
	if default_storage.exists(filepath):
		default_storage.delete(filepath)

# Deletes post and remove from s3 if it is a media post
def delete_post(post):
	classname = post.classname()
	if classname == "PhotoPost" or classname == "VideoPost" or classname == "AudioPost":
		filepath = post.url.replace(amazon_url,'')
		delete_from_s3(filepath)
		post.delete()
	else:
		post.delete()

#Gets every post type from a particular author and returns them in a list
#Not garunteed to be sorted
def get_post_list_by_author(author):
	textposts = list(author.textpost_set.all())
	photoposts = list(author.photopost_set.all())
	videoposts = list(author.videopost_set.all())
	audioposts = list(author.audiopost_set.all())
	return textposts + photoposts + videoposts + audioposts

# displays a users blog page if user exists
def blogpage(request,username):
	author = get_object_or_404(User,username=username)
	posts = get_post_list_by_author(author)

	# sort from oldest to newest, then reverse to get latest
	posts = reversed(sorted(posts, key=lambda post: post.post_date))
	return render_to_response('blog/blogpage.html',
							  {'author':author,
							   'posts':posts,},
							   context_instance=RequestContext(request))

@login_required(login_url='/login/')
def new_text_post(request):
	invalid = ""
	if request.method == 'POST':
		form = TextForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			slug = slugify(title)
			text = form.cleaned_data['text']	
			post = TextPost.objects.create(title=title,
										   slug=slug,
										   text=text,
										   author=request.user,)

			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No text in post"
	else:
		form = TextForm()
	
	return render_to_response('blog/textpost.html',
							  {'form':form, 'invalid':invalid},
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
			post.url = amazon_url + filepath
			post.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No Photo Selected"
	else:
		form = PhotoForm()
	return render_to_response('blog/photopost.html',
							  {'form':form, 'invalid':invalid},
							  context_instance=RequestContext(request))

@login_required(login_url='/login/')
def new_video_post(request):
	invalid = ""
	if request.method == 'POST':
		form = VideoForm(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES['video']
			description = form.cleaned_data['description']
			post = VideoPost.objects.create(filename=file.name,
										    url="",
											description=description,
											author=request.user)
			filepath = "%s/video/%s/%s" % (request.user.username, str(post.id), file.name)
			upload_to_s3(file, filepath)
			post.url = amazon_url + filepath
			post.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No Video Selected"
	else:
		form = VideoForm()
	return render_to_response('blog/videopost.html',
							  {'form':form, 'invalid':invalid},
							  context_instance=RequestContext(request))

@login_required(login_url='/login/')
def new_audio_post(request):
	invalid = ""
	if request.method == 'POST':
		form = AudioForm(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES['audio']
			description = form.cleaned_data['description']
			print description
			post = AudioPost.objects.create(filename=file.name,
										    url="",
											description=description,
											author=request.user)
			filepath = "%s/audio/%s/%s" % (request.user.username, str(post.id), file.name)
			upload_to_s3(file, filepath)
			post.url = amazon_url + filepath
			post.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No Audio Selected"
	else:
		form = AudioForm()
	return render_to_response('blog/audiopost.html',
							  {'form':form, 'invalid':invalid},
							  context_instance=RequestContext(request))
