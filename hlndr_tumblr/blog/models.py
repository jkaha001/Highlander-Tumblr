from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

# Create your models here.

class TextPost(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	text = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	tags = TaggableManager()

	def __unicode__(self):
		return "author:%s, title:%s, post_date:%s" % (self.author.username, 
													  self.title, 
													  self.post_date)

	def classname(self):
		return self.__class__.__name__

class PhotoPost(models.Model):
	filename = models.CharField(max_length=100)
	url = models.URLField()
	caption = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	tags = TaggableManager()

	def __unicode__(self):
		return "author:%s, filename:%s, post_date:%s" % (self.author.username,
													     self.filename,
														 self.post_date)

	def classname(self):
		return self.__class__.__name__

class VideoPost(models.Model):
	filename = models.CharField(max_length=100)
	url = models.URLField()
	description = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	tags = TaggableManager()

	def __unicode__(self):
		return "author:%s, filename:%s, post_date:%s" % (self.author.username,
													     self.filename,
														 self.post_date)

	def classname(self):
		return self.__class__.__name__

class AudioPost(models.Model):
	filename = models.CharField(max_length=100)
	url = models.URLField()
	description = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	tags = TaggableManager()

	def __unicode__(self):
		return "author:%s, filename:%s, post_date:%s" % (self.author.username,
													     self.filename,
														 self.post_date)

	def classname(self):
		return self.__class__.__name__

class QuotePost(models.Model):
	quote = models.TextField()
	source = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	tags = TaggableManager()

	def __unicode__(self):
		return "author:%s, post_date:%s" % (self.author.username, self.post_date)
	
	def classname(self):
		return self.__class__.__name__

class LinkPost(models.Model):
	title = models.CharField(max_length=100)
	link = models.URLField()
	description = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	tags = TaggableManager()

	def __unicode__(self):
		return "author:%s, title:%s, post_date:%s" % (self.author.username,
													  self.title,
													  self.post_date)
	def classname(self):
		return self.__class__.__name__

class ChatPost(models.Model):
	title = models.CharField(max_length=100)
	chat = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	tags = TaggableManager()

	def __unicode__(self):
		return "author:%s, title:%s, post_date:%s" % (self.author.username,
												      self.title,
													  self.post_date)
	def classname(self):
		return self.__class__.__name__
