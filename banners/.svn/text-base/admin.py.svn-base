# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.generic import (GenericTabularInline,
                                                 GenericStackedInline)
from django.contrib.contenttypes.models import ContentType
from django.forms import ModelForm

from smart_selects.form_fields import GenericChainedModelChoiceField

from models import BannerBlock, Banner, BannerItem


class BannerItemForm(ModelForm):

    object_id = GenericChainedModelChoiceField(queryset='',
                                               label=u'Цель баннера',
                                               chain_field='content_type',
                                               model_field='content_type',
                                               required=True)

    class Meta:
        model = BannerItem


class BannerItemInline(admin.TabularInline):
    model = BannerItem
    form = BannerItemForm


class BannerAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'type', 'banner_place', 'active',
                    'show_after', 'show_before')
    list_filter = ['active', 'banner_place']
    inlines = [BannerItemInline]


class BannerItemAdmin(admin.ModelAdmin):
    form = BannerItemForm

admin.site.register(Banner, BannerAdmin)
admin.site.register(BannerItem, BannerItemAdmin)
admin.site.register(BannerBlock)


class BannerItemForm(ModelForm):
    class Meta:
        model = BannerItem
        fields = ['banner', 'position']


class GenericBannerAdmin(GenericTabularInline):
    model = BannerItem
    form = BannerItemForm
    extra = 1
