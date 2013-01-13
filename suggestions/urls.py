from django.conf.urls import patterns, include, url

urlpatterns = patterns('suggestions.views',
    
    url(r'^$', 'suggestion'),
)