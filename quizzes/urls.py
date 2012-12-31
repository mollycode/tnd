from django.conf.urls import patterns, include, url

urlpatterns = patterns('quizzes.views',
    
    url(r'^$', 'get_out'),
)