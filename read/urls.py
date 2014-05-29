from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import read.views 
admin.autodiscover()
from read.forms import  TextForm, LoginForm, SettingsForm, UserForm
handler404 = 'mysite.views.errorpage'

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.htm	')),
	#url(r'^home/$', TemplateView.as_view(template_name='base.htm')),	
	url(r'^',include('django.contrib.auth.urls')),
	(r'^admin/', include(admin.site.urls)),

	#	(r'^home/$','home'),
)

urlpatterns += patterns('read.views',
	(r'^reader/$', 'speedreader'),
	(r'^memorize/$','memorize'),
	(r'^guest/$', 'testinput'),	
	(r'^settings/$','settings'),
	(r'^text/$','list'),
	(r'^createprofile/$','createprofile'),
	(r'^logout/$','logout'),
	(r'^search/$','search'),
	(r'^home/$','er'),
	(r'^$','er'),
)

urlpatterns += staticfiles_urlpatterns()
