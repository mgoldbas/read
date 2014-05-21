from django.shortcuts import render
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from read.forms import  TextForm, LoginForm, SettingsForm, UserForm
from registration.forms import RegistrationFormUniqueEmail
from read.models import MyUser, Text

# for splitting up text into sentences or list
import re
class Sentences:
	def __init__(self,text):
		count = 0
		word = []
		self.phrases = tuple(re.split("[.?]\s",text)) 
		for r in self.phrases:
			u = r.split(' ')
			word.append(u)
			count += 1
		self.words = word
		self.count = count

def chop(text):
	text = Sentences(text)
	
#page to display text in sentences with next button
def memorize(request):
	content = "Shall I compare thee to a summer's day? Thou art more lovely and more temperate. Rough winds do shake the darling buds of May. And summer's lease hath all too short a date. "
	test = Sentences(content)
	width = 300
	height = 400
	padding = 12
	font = 40
	#crappy version of time counter
	speed = self.count/60
	fill = {'word_list':test.phrases, 'title':"Speed Reader",'speed':speed, 'width':width, 'height':height,'padding':padding,'font':font,'rate':rate,'title':"home"}
	return render(request, 'SpeedReader/reader2.html',fill)
	
	
#page to display flasing text with next button


#list based home page
def home(request):
	buttons = [{'url':'textlist','name':'Reader'},{'url':'addtext','name':'Add Text'},{'url':'profile','name':'Settings'}]
	fill = {'buttons':buttons, 'user':request.user.is_authenticated(), 'title':'Home'}
	return render(request,'base.htm',fill)
	"""
	if request.user.is_authenticated():
		buttons = [{'url':'textlist','name':'Reader'},{'url':'addtext','name':'Add Text'},{'url':'profile','name':'Settings'}]
		fill = {'buttons':buttons, 'user':request.user.is_authenticated()}
		return render(request,'SpeedReader/baseboot.htm',fill)
	else:
		buttons = [{'url':'gtextlist','name':'Reader'}]
		fill = {'buttons':buttons,'user':request.user.is_authenticated()}
		return render(request,'SpeedReader/baseboot.htm',fill)
	"""

def guestlist(request):
	description = "SpeedReader Samples"
	Gamble = "They Don't Think It Be Like It Is, But It Do"
	Einstein = "And this, our life, exempt from public haunt, finds tongues in trees, books in the running brooks, sermons in stones, and good in everything."
	Lincoln = "America will never be destroyed from the outside. If we falter and lose our freedoms, it will be because we destroyed ourselves."
	Buddha = "Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared."
	t = {'Gamble':Gamble,'Einstein':Einstein,'Lincoln':Lincoln,'Buddha':Buddha}
	fill = {'texts':t,}
	return render(request, 'gtextlist.html', fill)

#login page
def login(request):
	if request.user.is_authenticated():
		return render(request, 'SpeedReader/loggedin.html')
	else:
		fill = {'fillform':LoginForm(), 'title' : "Login"}
		return render(request, 'form_base.html', fill)


		
#logout page
def logout(request):
	message="You have logged out"
	return render(request, 'message.htm',{'message':message})
	
	
#page for editing settings
def settings(request):
	errors = []
	if request.method =='POST':
		if not request.POST.get('first_name', ''):
			errors.append('Enter first name.')
		if not request.POST.get('last_name', ''):
			errors.append('Enter last name .')
	fill = {'fillform':SettingsForm(), 'title' : "Settings", 'errors':errors}
	return render(request, 'testform.htm', fill)
	
	
#page for creating a new profile
def createprofile(request):
	errors = []
	if request.method =='POST':
		if not request.POST.get('first_name', ''):
			errors.append('Enter first name.')
		if not request.POST.get('last_name', ''):
			errors.append('Enter last name .')
		if not request.POST.get('email'):
			errors.append('Enter email address')
		if not request.POST.get('password'):
			errors.append('Enter password')
	fill = {'fillform':UserForm(), 'title' : "Settings", 'errors':errors}
	return render(request, 'form_base.html', fill)


#main page with text
def list(request):
	t = ['Smile','Frown']
	description = '' 
	errors = []
	"""
	if request.method == 'GET': #Send information to reader or memorizer 
		name = request.GET['name']
		text = request.GET['text']
		section = Sentences(text)
		
	"""
	if request.META['HTTP_REFERER'] == "http://localhost:8000/home/": #Welcome the user on initial login 
		description = "Welcome Back"
	if request.META['HTTP_REFERER'] == "http://localhost:8000/createprofile/":
		if request.method == 'POST':
			form = UserForm(request.POST)
			if form.is_valid():
				new_user=form.save()	
				description = "Welcome %s! Begin speed reading and memorizing below" % new_user.username
			else:
				HttpResponseRedirect("/home")
				
	fill = {'listing':t, 'fillform':TextForm(), 'title':'Text', 'description':description}	
	if request.user.is_authenticated():
		return render(request, 'textlist.htm', fill)
	else:
		#fill = {'descrip':"Create an account to save text"}
		return render(request, 'textlist.htm', fill)

def speedreader(request):
	content = "hey whats up!!"
	n = []
	n = content.split(' ')
	setting = "large"
	if setting == "xsmall":
		width = 200
		height = 40
		padding = 10
		font = 30
	elif setting == "small":
		width = 250
		height = 50
		padding = 11
		font = 35
	elif setting == "med":
		width = 300
		height = 60
		padding = 12
		font = 40
	elif setting == "large":
		width = 350
		height = 80
		padding = 15
		font = 45
	elif setting == "xlarge":
		width = 400
		height = 80
		padding = 14
		font = 50
	speed = 300
	rate = 60000/(speed)
	fill = {'word_list':n, 'title':"Speed Reader",'speed':speed, 'width':width, 'height':height,'padding':padding,'font':font,'rate':rate}
	return render(request, 'read.htm',fill)
	
#guest speedreader page
def speedreader2(request):
	try:
		content = request.GET['text']
	except:
		content = "did not work"
	n = []
	n = content.split(' ')
	setting = "large"
	if setting == "xsmall":
		width = 200
		height = 40
		padding = 10
		font = 30
	elif setting == "small":
		width = 250
		height = 50
		padding = 11
		font = 35
	elif setting == "med":
		width = 300
		height = 60
		padding = 12
		font = 40
	elif setting == "large":
		width = 350
		height = 80
		padding = 15
		font = 45
	elif setting == "xlarge":
		width = 400
		height = 80
		padding = 14
		font = 50
	speed = 300 #Speed variable 
	rate = 60000/(speed) #Calculate WPM
	fill = {'word_list':n, 'title':"Speed Reader",'speed':speed, 'width':width, 'height':height,'padding':padding,'font':font,'rate':rate}
	return render(request, 'read.htm',fill)

#Memorize page	
def memorize2(request):
	try:
		content = request.GET['text']
	except:
		content = "did not work"
	n = []
	test = Sentences(content)
	width = 300
	height = 400
	padding = 12
	font = 40
	fill = {'word_list':test.phrases, 'title':"Reader", 'width':width, 'height':height,'padding':padding,'font':font,}
	return render(request, 'memorize.html',fill)	
	
def testinput(request):
	return render(request,'testinput.htm')		