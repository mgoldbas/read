from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import read.views 
admin.autodiscover()
from read.forms import  TextForm, LoginForm, SettingsForm, UserForm

fill = {'createform':UserForm(),'loginform':LoginForm()}
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.htm'),fill),
	url(r'^home/$', TemplateView.as_view(template_name='base.htm'), fill),	
	url(r'^',include('django.contrib.auth.urls')),
)


	

urlpatterns += patterns('read.views',
	(r'^reader/$', 'speedreader'),
	(r'^reader2/$','speedreader2'),
	(r'^memorize2/$','memorize2'),
	(r'^guest/$', 'testinput'),	
	(r'^gtextlist/$','guestlist'),
	(r'^settings/$','settings'),
	(r'^text/$','list'),
	(r'^createprofile/$','createprofile'),
)

urlpatterns += staticfiles_urlpatterns()
