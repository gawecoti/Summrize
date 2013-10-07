# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Text.title'
        db.add_column(u'text_text', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Text', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Text.title'
        db.delete_column(u'text_text', 'title')


    models = {
        u'text.text': {
            'Meta': {'object_name': 'Text'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Text'", 'max_length': '255'})
        }
    }

    complete_apps = ['text']