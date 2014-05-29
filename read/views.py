from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from read.forms import  TextForm, LoginForm, SettingsForm, UserForm, FileForm
from registration.forms import RegistrationFormUniqueEmail
from read.models import MyUser, Text
from read.functions import chunks

# for splitting up text into sentences or list
import re, string
class Sentences:
	def __init__(self,text):
		count = 0
		word = []
		self.phrases = tuple(re.split("[.?]\s",text)) #self.phrases is an array of sentences 
		for r in self.phrases:
			u = r.split(' ')
			word.append(u)
			count += 1
		self.words = word #self.words is an array of words
		self.count = count #self.count is the number of words
	
#logout page
def logout(request):
	message="You have logged out"
	return render(request, 'message.htm',{'message':message})

	
def er(request):
	if request.method == 'POST':
		form=UserForm(request.POST)
		if form.is_valid():
			clean = form.cleaned_data()
			account = MyUser(clean)
			account.save()
	return render(request,'base.htm')
	
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
	if request.user.is_authenticated():
		t = Text.objects.filter(user=request.user)
		description = ''
		errors = []
		if "/login/" in request.META['HTTP_REFERER']:  #Welcome the user on initial login 
			description = "Welcome Back!"
		if "/createprofile/" in request.META['HTTP_REFERER']:  #Welcome new users
			description = "Welcome to Speedreader!"
		if request.method == 'POST': #adding new text or file ------ HELP GEOFF!!!!
			if request.POST['type'] == 'text': #for uploading text
				form= TextForm(request.POST)
				if form.is_valid():
					group = chunks(str(request.POST['text']))
					if len(group) == 1: # if text does not need to be chopped up
						text = Text(name=request.POST['name'],text=request.POST['text'],user=request.user)
						text.save()	
						description = "Text Uploaded successfully"
					else:
						c = 0
						while c < len(group):
							new_name = str(request.POST['name']) + "(" + str(c + 1) + ")"
							text = Text(name=new_name, text=group[c],user=request.user)
							text.save()
							c += 1
						description = "Text partitioned into smaller segments"
			if request.POST['type'] == 'file': #for uploading files
				form= FileForm(request.POST)	
				if form.is_valid():
					group = chunks(str(form['text'])) #chop up text 
					if len(group) == 1: # if text does not need to be chopped up
						text = Text(name=request.POST['name'],text=request.POST['text'],user=request.user)
						text.save()
						description = "Text Uploaded successfully"
					else:
						c = 0
						while c < len(group):
							new_name = str(request.POST['name']) + "(" + str(c + 1) + ")"
							text = Text(name=new_name, text=group[c],user=request.user)
							text.save()
							c += 1
						description = "Text partitioned into smaller segments"
							

		if "/text" in request.META['HTTP_REFERER']:
			if request.method == 'GET':
				try:
					id = request.GET['id']
					r = Text.objects.get(pk=id)
					r.delete()
					description = "Text deleted."
				except:
					pass
			
		fill = {'listing':t, 'textform':TextForm(), 'fileform':FileForm(),'title':'Text', 'description':description}	
		return render(request, 'textlist.htm', fill)
	else:
		fill = {'message':"Create an account to save text"}
		return render(request, 'message.htm', fill)


	
#guest speedreader page
def speedreader(request): #add  Text model id in url to return page
	if "/text/" in request.META['HTTP_REFERER']: 
		id = request.GET['id']
		t = Text.objects.get(pk=id)
		content = t.text
	if "/guest/" in request.META['HTTP_REFERER']:
		try:
			content = request.GET['text']
		except:
			content = "hey whats up"
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
def memorize(request):
	if "/text/" in request.META['HTTP_REFERER']: 
		id = request.GET['id']
		t = Text.objects.get(pk=id)
		content = t.text
	if "/guest/" in request.META['HTTP_REFERER']:
		try:
			content = request.GET['text']
		except:
			content = "hey whats up"
	n = []
	text = Sentences(content)
	width = 300
	height = 400
	padding = 12
	font = 40
	fill = {'word_list':text.phrases, 'title':"Reader", 'width':width, 'height':height,'padding':padding,'font':font,}
	return render(request, 'memorize.html',fill)	

#Guest page for trying out functionality
def testinput(request): 
	return render(request,'testinput.htm')		
	
def errorpage(request):
	fill = {'message':'HTTP 404 Page Not Found'}
	return render(request,'message.htm',fill)
	
def search(request):
	if 'searcher' in request.GET:
		lookup = request.GET['searcher']
		message = "You search for: %r " % lookup
		searched = request.GET['searcher']
		material = Text.objects.filter(name=searched)
	else:
		message = "You submitted a blank form" 
	fill = {'message':message,'texts':material}
	return render(request,'search.htm',fill)
		
		