from django.db import models
from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
import datetime

# Create your models here.

#first create a friendship class to specify that a user can have friends
class Friendship(models.Model):
	#from_friend is the friendship initiator and to get all users current friends do <user>.from_friend_set.all()
	from_friend = models.ForeignKey(User, related_name='from_friend_set')
	
	#to_friend is who we want to be friends with and to see all users who are friends with this user do <user>.to_friend_set.all()
	to_friend = models.ForeignKey(User, related_name='to_friend_set')
	
	#attribute to show when friendship was created
	friend_since = models.DateTimeField(auto_now_add=True, editable=False)
	
	def __unicode__(self):
		return u'from_friend: %s, to_friend: %s, friendSince: %s' % (self.from_friend.username, self.to_friend.username, self.friend_since)

	class Meta:
		#this will make sure the from_friend and to_friend are unique
		unique_together = (('from_friend', 'to_friend'),)

class FriendRequest(models.Model):
	sender = models.ForeignKey(User, related_name='invite_sender')
	reciever = models.ForeignKey(User, related_name='invite_reciever')
	time_sent = models.DateTimeField(auto_now_add=True, editable=False)
	
	def __unicode__(self):
		return u'Invitation sent from <%s> to <%s> at <%s>' % (self.sender.username, self.reciever.username, self.time_sent)

	class Meta:
		unique_together = (('sender', 'reciever'),)

	#function to create a friend request (doesnt add friend)
	#def send_friend_request(self):
		#friendMaker = self.sender
		#friendReciever = self.reciever

		#might need to create url path to the recievers friends notifications

		#context = Context({
		#	'sender': friendMaker,
		#	'reciever': friendReciever
		#	})


	def accept(self):
		sender=self.sender
		reciever = self.reciever
	
		#create mutual friendship
		friendship1 = Friendship(from_friend=sender, to_friend=reciever)
		friendship2 = Friendship(from_friend=reciever, to_friend=sender)
		friendship1.save();
		friendship2.save();

		#remove the Friend Request object
		fr = FriendRequest.objects.filter(sender=sender, reciever=reciever)
		#remove or set flag that says these two are friends
		fr.delete()
		fr = None

	def deny(self):
		sender = self.sender
		reciever = self.reciever

		fr = FriendRequest.objects.filter(sender=sender, reciever=reciever)
		fr.delete()

