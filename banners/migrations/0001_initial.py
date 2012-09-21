# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table('banners_banner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_after', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('show_before', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('shows_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('banner_place', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('banners', ['Banner'])

        # Adding model 'BannerItem'
        db.create_table('banners_banneritem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='banner_target_set', to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['banners.Banner'])),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('banners', ['BannerItem'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table('banners_banner')

        # Deleting model 'BannerItem'
        db.delete_table('banners_banneritem')


    models = {
        'banners.banner': {
            'Meta': {'ordering': "['title']", 'object_name': 'Banner'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banner_place': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_after': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'show_before': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'shows_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'banners.banneritem': {
            'Meta': {'ordering': "['banner__title']", 'object_name': 'BannerItem'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['banners.Banner']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banner_target_set'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['banners']