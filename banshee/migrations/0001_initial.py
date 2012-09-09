# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table('banshee_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('banshee', ['Artist'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table('banshee_artist')


    models = {
        'banshee.artist': {
            'Meta': {'object_name': 'Artist'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['banshee']