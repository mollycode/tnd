from django.conf.urls import patterns, include, url

urlpatterns = patterns('courses.views',

    url(r'^(?P<course_id>\d+)/(?P<night_num>\d+)/(?P<clip_num>\d+)/$', 'course'),
    url(r'^(?P<course_id>\d+)/$', 'bare_course'),
    url(r'^(?P<course_id>\d+)/info/$', 'info'),
    url(r'^(?P<course_id>\d+)/discussion/$', 'discussion'),
    
    # temporary course pages
    
    url(r'^cambroncourseinfo/$', 'cambron'),
    url(r'^ciofficourseinfo/$', 'cioffi'),
    url(r'^foxcourseinfo/$', 'fox'),
    url(r'^glasscourseinfo/$', 'glass'),
    
    url(r'^$', 'get_out'),
)