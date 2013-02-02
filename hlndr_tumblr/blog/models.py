from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
"""
class Blog(models.Model):
	user = models.ForeignKey(User)
"""

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	text = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def classname(self):
		return self.__class__.__name__

class PhotoPost(models.Model):
	filename = models.CharField(max_length=100)
	url = models.URLField()
	caption = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)

	def __unicode__(self):
		return self.filename

	def classname(self):
		return self.__class__.__name__

"""
class Hashtag(models.Model):
	name = models.CharField(max_length=50)
	post = models.ForeignKey(Post)
"""

	
