"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from banners.models import Banner, BannerItem


class BannerTest(TestCase):
    fixtures = ['test_data.yaml']

    def setUp(self):
        self.user = User.objects.get()
        self.banner = Banner.objects.get()
        self.item = BannerItem.objects.create(banner=self.banner,
                                              content_type=ContentType.objects.get_for_model(self.user),
                                              object_id=1)

    def test_banners(self):
        self.assertEqual(Banner.objects.get_for_target(target=self.user)[0], self.banner)
