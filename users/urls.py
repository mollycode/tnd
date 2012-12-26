from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^login/$', 'users.views.login'),
    url(r'^profile/$', 'users.views.profile'),
    url(r'^register/$', 'users.views.register'),
    
    url(r'^logout/$', 'users.views.logout'),
)