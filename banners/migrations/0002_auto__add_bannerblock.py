# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BannerBlock'
        db.create_table('banners_bannerblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('banners', ['BannerBlock'])


    def backwards(self, orm):
        
        # Deleting model 'BannerBlock'
        db.delete_table('banners_bannerblock')


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
