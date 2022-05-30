# 一定要使用django.test(不要使用unittest),否则某些功能无法使用
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

from django.urls import reverse

from scoreImprover.models import NeepStudy
from user.models import User
from user.views import uob
from word.models import NeepWordsReq
from word.views import wob, neepob

client = APIClient()


# pmg test scoreImprover.tests.test_urls.ImproverUrlsTestCase
class ImproverUrlsTestCase(TestCase):
    # 一般的,由DRF生成的api路由,只要一个没有问题,那么其余4个都不会有问题(尤其指的是ModelViewSet&register注册的路由)
    def test_neep_list(self):
        url = reverse('improver:neep-list')
        self.assertEqual(url, '/improver/neep/')

    def test_cet4_list(self):
        url = reverse('improver:cet4-list')
        self.assertEqual(url, '/improver/cet4/')

    def test_cet6_list(self):
        url = reverse('improver:cet6-list')
        self.assertEqual(url, '/improver/cet6/')

    def test_neep_detail(self):
        url = reverse('improver:neep-detail', args=["1"])
        self.assertEqual(url, '/improver/neep/1/')

    def test_cet4_detail(self):
        url = reverse('improver:cet4-detail', args=["1"])
        self.assertEqual(url, '/improver/cet4/1/')

    def test_cet6_detail(self):
        url = reverse('improver:cet6-detail', args=["1"])
        self.assertEqual(url, '/improver/cet6/1/')

    # 下面测试自定义的零碎路由
    # pmg test scoreImprover.tests.test_urls.ImproverUrlsTestCase --keepdb
    def test_sized_review(self):
        url = reverse('improver:sized_review', args=["cet4", "10"])
        self.assertEqual(url, '/improver/review/cet4/10/')
        url = reverse('improver:sized_review', args=["cet6", "10"])
        self.assertEqual(url, '/improver/review/cet6/10/')
        url = reverse('improver:sized_review', args=["neep", "10"])
        self.assertEqual(url, '/improver/review/neep/10/')

    def test_study_refresh(self):
        url = reverse('improver:refresh', args=["cet4"])
        self.assertEqual(url, '/improver/study/cet4/')
