# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.functional import lazy

IMAGE = 0
FLASH = 1
BANNER_TYPES = ((IMAGE, u"Картинка"),
                (FLASH, u"Флэш"),
                )
BANNER_WIDGETS = {IMAGE: 'banners/imagetype.html',
                  FLASH: 'banners/flashtype.html'
                 }

# TODO banner_type is model and subclassing it


class BannerBlock(models.Model):
    title = models.CharField(u'Название', max_length=100)

    width = models.PositiveIntegerField(u"Ширина",
                                        blank=True, null=True)
    height = models.PositiveIntegerField(u"Высота",
                                        blank=True, null=True)

    class Meta:
        verbose_name = u'Место для баннера'
        verbose_name_plural = u'Места для баннеров'
        ordering = ['title',]

    def __unicode__(self):
        return self.title


class BannerManager(models.Manager):

    def _get_for_target(self, target):

        target_type = ContentType.objects.get_for_model(target)
        today = datetime.today()
        banners = self.get_query_set().filter(active=True,
                                              items__content_type=target_type,
                                              items__object_id=target.id,
                                              )
        date_filters = (Q(show_after__isnull=True)|\
                        Q(show_after__lte=today))&\
                       (Q(show_before__isnull=True)|\
                        Q(show_before__gte=today))
        banners = banners.filter(date_filters).distinct()\
                         .order_by('items__position')

        return banners

    def get_for_target(self, target, soft=True):

        banners = self._get_for_target(target)
        if not soft or banners or not hasattr(target, '_tree_manager'):
            return banners

        parent_attr = getattr(target._meta, 'parent_attr', 'parent')

        parent = getattr(target, parent_attr, None)
        while not banners and parent:
            banners = self._get_for_target(parent)
            parent = getattr(parent, parent_attr, None)

        return banners


class Banner(models.Model):

    title = models.CharField(u'Название', max_length=100)
    active = models.BooleanField(u'Активно', default=False)
    show_after = models.DateField(u'Дата начала показов',
                                  blank=True, null=True)
    show_before = models.DateField(u'Дата конца показов',
                                   blank=True, null=True)

    type = models.IntegerField(u"Тип", default=0, choices=BANNER_TYPES)
    file = models.FileField(u"Файл", upload_to='images/banners')

    shows_count = models.PositiveIntegerField(u"Количество показов", default=0)
    banner_place = models.ForeignKey(BannerBlock, verbose_name=u"Место размещения")

    width = models.PositiveIntegerField(u"Ширина", blank=True, null=True)
    height = models.PositiveIntegerField(u"Высота", blank=True, null=True)

    objects = BannerManager()

    class Meta:
        verbose_name = u'Баннер'
        verbose_name_plural = u'Баннеры'
        ordering = ['title',]

    def __unicode__(self):
        return self.title

    def get_size_attr(self, attr):
        banner_place_attr = getattr(self.banner_place, attr) or 0
        self_attr = getattr(self, attr) or 0

        return min(banner_place_attr,
                   self_attr) or self_attr or banner_place_attr

    def get_height(self):
        return self.get_size_attr('height')

    def get_width(self):
        return self.get_size_attr('width')

    def get_size(self):
        return ''.join([x for x in [self.get_width(), 'x', self.get_height()]])

    @property
    def template(self):
        return BANNER_WIDGETS[self.type]


class BannerTargets(dict):

    def register(self, model):
        self[model._meta.object_name.lower()] = model

        model.banners = generic.GenericRelation(BannerItem)

        def get_banners(self):
            return Banner.objects.get_for_target(self)

        model.get_banners = get_banners

BannerTargets = BannerTargets()

targets = lazy(lambda: BannerTargets.keys(), list)


class BannerItem(models.Model):

    content_type = models.ForeignKey(ContentType,
                                     verbose_name=u'Тип цели',
                                     limit_choices_to={
                                         'model__in': targets
                                     },
                                     related_name="banner_target_set")
    object_id = models.PositiveIntegerField(u"ИД цели")

    target = generic.GenericForeignKey()

    banner = models.ForeignKey(Banner,
                               verbose_name=u"Баннер",
                               related_name='items')

    position = models.PositiveIntegerField(u"Порядок", default=100)

    class Meta:
        verbose_name = u'Отношение Баннер - Цель'
        verbose_name_plural = u'Отношения Баннер - Цель'
        ordering = ['banner__title',]

    def __unicode__(self):
        return u'Баннер %s показывается на %s' % (self.banner,
                                                  self.target)
