# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Character.notes'
        db.alter_column('kana_character', 'notes', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Character.notes'
        db.alter_column('kana_character', 'notes', self.gf('django.db.models.fields.TextField')(default=None))

    models = {
        'kana.character': {
            'Meta': {'object_name': 'Character'},
            'gojuon_col': ('django.db.models.fields.IntegerField', [], {}),
            'gojuon_row': ('django.db.models.fields.IntegerField', [], {}),
            'hiragana': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dakuten': ('django.db.models.fields.BooleanField', [], {}),
            'is_handakuten': ('django.db.models.fields.BooleanField', [], {}),
            'is_yoon': ('django.db.models.fields.BooleanField', [], {}),
            'katakana': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'romaji': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True'})
        }
    }

    complete_apps = ['kana']