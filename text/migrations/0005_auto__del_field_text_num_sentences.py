# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Text.num_sentences'
        db.delete_column(u'text_text', 'num_sentences')


    def backwards(self, orm):
        # Adding field 'Text.num_sentences'
        db.add_column(u'text_text', 'num_sentences',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)


    models = {
        u'text.text': {
            'Meta': {'object_name': 'Text'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mean_scored_text': ('django.db.models.fields.TextField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Text'", 'max_length': '255'}),
            'top_n_scored_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['text']