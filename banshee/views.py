# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
from banshee.models import Artist
from banshee.forms import ArtistForm


class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/list.html'
    paginate_by = 10


class ArtistCreateView(CreateView):
    model = Artist
    template_name = 'artists/create.html'
    form_class = ArtistForm

    def get_success_url(self):
        return reverse('artist_list')


class ArtistUpdateView(UpdateView):
    model = Artist
    template_name = 'artists/edit.html'
    form_class = ArtistForm

    def get_success_url(self):
        return reverse('artist_list')

