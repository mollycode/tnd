from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^(?P<course_id>\d+)/(?P<night>\d+)/$', 'courses.views.course'),
    
    # temporary course pages
    
    url(r'^cambroncourseinfo/$', 'courses.views.cambron'),
    url(r'^ciofficourseinfo/$', 'courses.views.cioffi'),
    url(r'^foxcourseinfo/$', 'courses.views.fox'),
    url(r'^glasscourseinfo/$', 'courses.views.glass'),
)