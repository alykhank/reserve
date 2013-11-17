from django.conf.urls import patterns, url

from claim import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^claim/(?P<pk>\d+)/$', views.claim, name='claim'),
	url(r'^release/(?P<pk>\d+)/$', views.release, name='release'),
)
