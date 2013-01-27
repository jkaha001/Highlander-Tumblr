from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
  	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
    
	user = models.OneToOneField(User)
	# URL to avatar image hosted
	avatar = models.CharField(max_length=200)
	nickname = models.CharField(max_length=30, blank=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
	birthday = models.DateField()
	interests = models.CharField(max_length=300, blank=True)
	
	def __unicode__(self):
		return user.username

"""
def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
"""
