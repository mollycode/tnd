from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',

    url(r'^login/$', 'login'),
    url(r'^profile/$', 'profile'),
    url(r'^register/$', 'register'),
    url(r'^currentlessons/$', 'currentlessons'),
    url(r'^completedcourses/$', 'completedcourses'),
    
    url(r'^addcourse/(?P<course_id>\d+)/$', 'addcourse'),
    url(r'^removecourse/(?P<course_id>\d+)/$', 'removecourse'),
    url(r'^finishcourse/(?P<course_id>\d+)/$', 'finishcourse'),
    
    url(r'^logout/$', 'logout'),
    
    url(r'^$', 'redirector'),
)