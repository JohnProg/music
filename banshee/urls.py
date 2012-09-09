from django.conf.urls import patterns, include, url
from banshee import views as v

urlpatterns = patterns('',
    url(r'^artist/create/$', v.ArtistCreateView.as_view(), name='artist_create'),
    url(r'^artist/edit/(?P<pk>\d+)$', v.ArtistUpdateView.as_view(), name='artist_edit'),
    url(r'^artist/list/$', v.ArtistListView.as_view(), name='artist_list'),

)
