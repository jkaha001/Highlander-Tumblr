from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
  	GENDER_CHOICES = (
		('u', 'Undisclosed'),
		('m', 'Male'),
		('f', 'Female'),
	)
    
	user = models.OneToOneField(User)

	# URL to avatar image hosted
	avatar = models.URLField()
	nickname = models.CharField(max_length=50, blank=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
	birthday = models.DateField()
	interests = models.CharField(max_length=500, blank=True)
	
	def __unicode__(self):
		return user.username
