from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^profile/$', 'users.views.profile'),
    url(r'^register/$', 'users.views.register'),
)