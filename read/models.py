from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(User):
	speed = models.IntegerField()
	size = models.CharField(max_length=30)
    #def __unicode__(self):
	#	return u'%s %s' % (self.first_name, self.last_name)

class Text(models.Model):
	user = models.ForeignKey(MyUser, related_name="words")
	name = models.CharField(max_length=30)
	text = models.CharField(max_length=100000)
	def __unicode__(self):
		return self.name
	
