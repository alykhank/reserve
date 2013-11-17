from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'reserve.views.home', name='home'),
    url(r'^', include('claim.urls', namespace='claim')),

    url(r'^admin/', include(admin.site.urls)),
)
