from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(User):	
	"""
	username = models.CharField(null=False, max_length=30)
	password = models.CharField(null=False, max_length=30)
	email = models.EmailField()"""
	speed = models.IntegerField()
	size = models.CharField(max_length=30)
    #def __unicode__(self):
	#	return self.username

class Text(models.Model):
	user = models.ForeignKey(MyUser)
	name = models.CharField(max_length=30)
	text = models.CharField(max_length=100000)
	def __unicode__(self):
		return self.name
	
