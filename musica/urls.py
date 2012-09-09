from django.conf.urls import patterns, include, url
from django.contrib.staticfiles import urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musica.views.home', name='home'),
    # url(r'^musica/', include('musica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^banshee/', include('banshee.urls')),
)


urlpatterns += urls.staticfiles_urlpatterns()