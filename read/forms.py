
from django.contrib.auth.forms import UserCreationForm
from read.models import Text, MyUser
from django import forms


 
SIZE = [('Xsmall', 'Xsmall'),('Small', 'Small'),('Medium', 'Medium'),('Large','Large'),('Xlarge','Xlarge')]

class TextForm(forms.Form):
	name = forms.CharField()
	text = forms.CharField(widget=forms.Textarea, label="Add Text")

class FileForm(forms.Form):
	name = forms.CharField()
	file = forms.FileField()
	
class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField()

class UserForm(forms.ModelForm):
	r = 100
	SPEEDS = []
	while r != 900:
		rate = 60000/(r) #Calculate WPM
		choice = (rate,r)
		SPEEDS.append(choice)
		r += 100
	class Meta:
		model = MyUser
	RATES = tuple(SPEEDS)
	speed = forms.ChoiceField(choices=RATES, initial=300)
	size = forms.ChoiceField(choices=SIZE, widget=forms.RadioSelect(), label="Text Size", initial="med")
	#paid = forms.ChoiceField(choices=PAID,widget=forms.RadioSelect(), label="Premium account?")
	

class SettingsForm(forms.Form):
	speed = forms.IntegerField()
	size = forms.ChoiceField(choices=SIZE,widget=forms.RadioSelect(), label="Size")
	#paid = forms.ChoiceField(choices=PAID,widget=forms.RadioSelect(), label="Premium account?")