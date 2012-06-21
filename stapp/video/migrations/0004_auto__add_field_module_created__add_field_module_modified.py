# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Module.created'
        db.add_column('video_module', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 6, 21, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Module.modified'
        db.add_column('video_module', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 6, 21, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Module.created'
        db.delete_column('video_module', 'created')

        # Deleting field 'Module.modified'
        db.delete_column('video_module', 'modified')


    models = {
        'video.module': {
            'Meta': {'object_name': 'Module'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'vidio_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['video.Video']", 'symmetrical': 'False'})
        },
        'video.video': {
            'Meta': {'object_name': 'Video'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['video']