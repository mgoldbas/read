
from read.forms import  TextForm, LoginForm, SettingsForm, UserForm
from django.views.generic.edit import FormView

class MemberFormView(FormView):
	errors = []
	template_name = "Member_edit.html"
	success_url = '/thanks/'

class GuestFormView(FormView):
	errors = []
	template_name = "Guest.html"
	
class UserView(MemberFormView):
	form_class = UserForm
	def post(self):
		if not self.get('first_name'):
			self.errors.append("First Name")
		if not self.get('last_name'):
			self.errors.append("Last Name")
		if not self.get("email"):
			self.errors.append("Email")
		if not self.get("password"):
			self.errors.append("Password")

class LoginView(GuestFormView):
	form_class = LoginForm
	def post(self):
		
