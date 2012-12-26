from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'main.views.home'),
    url(r'^personalpage/$', 'main.views.personalpage'),
    url(r'^about/$', 'main.views.about'),

    url(r'^courselist/$', 'main.views.courselist'),
    url(r'^wiki/$', 'main.views.wiki'),
    
    url(r'^users/', include('users.urls')),
    
    url(r'^course/', include('courses.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
