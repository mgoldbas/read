from django import forms
from django.contrib.auth.forms import UserCreationForm
from read.models import Text, MyUser
 
SIZE = [('Xsmall', 'Xsmall'),('Small', 'Small'),('Medium', 'Medium'),('Large','Large'),('Xlarge','Xlarge')]

class TextForm(forms.Form):
	name = forms.CharField()
	text = forms.CharField(widget=forms.Textarea, label="Add Text")
	file = forms.FileField()
	
class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField()

class UserForm(UserCreationForm):
	r = 100
	SPEEDS = []
	while r != 900:
		rate = 60000/(r) #Calculate WPM
		choice = (rate,r)
		SPEEDS.append(choice)
		r += 100
	RATES = tuple(SPEEDS)
	username = forms.EmailField(help_text=("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),label="Email")
	first_name = forms.CharField()
	last_name = forms.CharField()
	speed = forms.ChoiceField(choices=RATES)
	size = forms.ChoiceField(choices=SIZE, widget=forms.RadioSelect(), label="Text Size")
	#paid = forms.ChoiceField(choices=PAID,widget=forms.RadioSelect(), label="Premium account?")
	

class SettingsForm(forms.Form):
	speed = forms.IntegerField()
	size = forms.ChoiceField(choices=SIZE,widget=forms.RadioSelect(), label="Size")
	#paid = forms.ChoiceField(choices=PAID,widget=forms.RadioSelect(), label="Premium account?")