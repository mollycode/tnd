from django.conf.urls import patterns, include, url

urlpatterns = patterns('quizzes.views',
    
    url(r'^example/$', 'example'),
    
    url(r'^$', 'get_out'),
)