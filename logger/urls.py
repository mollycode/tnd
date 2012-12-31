from django.conf.urls import patterns, include, url

urlpatterns = patterns('logger.views',

    # for reference
    # url(r'^(?P<course_id>\d+)/(?P<night_num>\d+)/(?P<clip_num>\d+)/$', 'course'),

    url(r'^$', 'get_out'),
)