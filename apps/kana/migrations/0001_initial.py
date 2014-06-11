# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Character'
        db.create_table('kana_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('romaji', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('hiragana', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('katakana', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('is_plain', self.gf('django.db.models.fields.BooleanField')()),
            ('is_dakuten', self.gf('django.db.models.fields.BooleanField')()),
            ('is_handakuten', self.gf('django.db.models.fields.BooleanField')()),
            ('is_yoon', self.gf('django.db.models.fields.BooleanField')()),
            ('gojuon_row', self.gf('django.db.models.fields.IntegerField')()),
            ('gojuon_col', self.gf('django.db.models.fields.IntegerField')()),
            ('alternate_romaji', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, default=None, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, default=None, blank=True)),
        ))
        db.send_create_signal('kana', ['Character'])


    def backwards(self, orm):
        # Deleting model 'Character'
        db.delete_table('kana_character')


    models = {
        'kana.character': {
            'Meta': {'object_name': 'Character'},
            'alternate_romaji': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'default': 'None', 'blank': 'True'}),
            'gojuon_col': ('django.db.models.fields.IntegerField', [], {}),
            'gojuon_row': ('django.db.models.fields.IntegerField', [], {}),
            'hiragana': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dakuten': ('django.db.models.fields.BooleanField', [], {}),
            'is_handakuten': ('django.db.models.fields.BooleanField', [], {}),
            'is_plain': ('django.db.models.fields.BooleanField', [], {}),
            'is_yoon': ('django.db.models.fields.BooleanField', [], {}),
            'katakana': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'romaji': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['kana']