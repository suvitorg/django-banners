# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Renaming column for 'Banner.banner_place' to match new field type.
        db.rename_column('banners_banner', 'banner_place', 'banner_place_id')
        # Changing field 'Banner.banner_place'
        db.alter_column('banners_banner', 'banner_place_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banners.BannerBlock']))

        # Adding index on 'Banner', fields ['banner_place']
        db.create_index('banners_banner', ['banner_place_id'])


    def backwards(self, orm):
        
        # Removing index on 'Banner', fields ['banner_place']
        db.delete_index('banners_banner', ['banner_place_id'])

        # Renaming column for 'Banner.banner_place' to match new field type.
        db.rename_column('banners_banner', 'banner_place_id', 'banner_place')
        # Changing field 'Banner.banner_place'
        db.alter_column('banners_banner', 'banner_place', self.gf('django.db.models.fields.IntegerField')())


    models = {
        'banners.banner': {
            'Meta': {'ordering': "['title']", 'object_name': 'Banner'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banner_place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banners.BannerBlock']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_after': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'show_before': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'shows_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'banners.bannerblock': {
            'Meta': {'ordering': "['title']", 'object_name': 'BannerBlock'},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
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
