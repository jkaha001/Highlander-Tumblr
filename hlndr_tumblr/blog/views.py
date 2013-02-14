# Create your views here
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import TextPost, PhotoPost, VideoPost, AudioPost, QuotePost, LinkPost, ChatPost
from blog.forms import TextForm, PhotoForm, VideoForm, AudioForm, QuoteForm, LinkForm, ChatForm
from utils.shortcuts import *

import threading

amazon_url = "https://s3-us-west-1.amazonaws.com/highlander-tumblr-test-bucket/"

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
			tags = form.cleaned_data['tags']
				
			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No text in post"
	else:
		form = TextForm()
	
	return render_to_response('blog/textform.html',
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
			tags = form.cleaned_data['tags']

			filepath = "%s/image/%s/%s" % (request.user.username, str(post.id), file.name)
			s3_thread(file, filepath)
			post.url = amazon_url + filepath
			post.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No Photo Selected"
	else:
		form = PhotoForm()
	return render_to_response('blog/photoform.html',
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
			tags = form.cleaned_data['tags']

			filepath = "%s/video/%s/%s" % (request.user.username, str(post.id), file.name)
			s3_thread(file, filepath)
			post.url = amazon_url + filepath
			post.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No Video Selected"
	else:
		form = VideoForm()
	return render_to_response('blog/videoform.html',
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
			tags = form.cleaned_data['tags']

			filepath = "%s/audio/%s/%s" % (request.user.username, str(post.id), file.name)
			s3_thread(file, filepath)
			post.url = amazon_url + filepath
			post.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No Audio Selected"
	else:
		form = AudioForm()
	return render_to_response('blog/audioform.html',
							  {'form':form, 'invalid':invalid},
							  context_instance=RequestContext(request))

@login_required(login_url='/login/')
def new_quote_post(request):
	invalid = ""
	if request.method == 'POST':
		form = QuoteForm(request.POST)
		if form.is_valid():
			quote = form.cleaned_data['quote']
			source = form.cleaned_data['source']
			post = QuotePost.objects.create(quote=quote,
										    source=source,
											author=request.user)
			tags = form.cleaned_data['tags']

			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No quote in post"
	else:
		form = QuoteForm()
	return render_to_response('blog/quoteform.html',
							  {'form':form, 'invalid':invalid},
							  context_instance=RequestContext(request))

@login_required(login_url='/login/')
def new_link_post(request):
	invalid = ""
	if request.method == 'POST':
		form = LinkForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			link = form.cleaned_data['link']
			description = form.cleaned_data['description']
			post = LinkPost.objects.create(title=title,
										   link=link,
										   description=description,
										   author=request.user)
			tags = form.cleaned_data['tags']

			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No link in post"
	else:
		form = LinkForm()
	return render_to_response('blog/linkform.html',
							  {'form':form, 'invalid':invalid},
							  context_instance=RequestContext(request))

@login_required(login_url='/login/')
def new_chat_post(request):
	invalid = ""
	if request.method == 'POST':
		form = ChatForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			chat = form.cleaned_data['chat']
			post = ChatPost.objects.create(title=title,
										   chat=chat,
										   author=request.user)
			tags = form.cleaned_data['tags']

			return HttpResponseRedirect('/dashboard/')
		else:
			invalid = "No chat in post"
	else:
		form = ChatForm()
	return render_to_response('blog/chatform.html',
							  {'form':form, 'invalid':invalid},
							  context_instance=RequestContext(request))

