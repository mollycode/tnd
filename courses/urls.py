from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^(?P<course_id>\d+)/(?P<night>\d+)/(?P<clip>\d+)/$', 'courses.views.course'),
    url(r'^(?P<course_id>\d+)/info/$', 'courses.views.info'),
    url(r'^(?P<course_id>\d+)/discussion/$', 'courses.views.discussion'),
    
    # temporary course pages
    
    url(r'^cambroncourseinfo/$', 'courses.views.cambron'),
    url(r'^ciofficourseinfo/$', 'courses.views.cioffi'),
    url(r'^foxcourseinfo/$', 'courses.views.fox'),
    url(r'^glasscourseinfo/$', 'courses.views.glass'),
    
    url(r'^$', 'courses.views.get_out'),
)