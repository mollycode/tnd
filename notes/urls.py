from django.conf.urls import patterns, include, url

urlpatterns = patterns('notes.views',

    url(r'^mynotes/$', 'my_notes'),
    url(r'^$', 'get_out'),
)