# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from banshee.models import Artist


class ArtistForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        super(ArtistForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Artist