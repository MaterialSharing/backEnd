from django.test import TestCase
from rest_framework.reverse import reverse


class UserUrlTestCase(TestCase):
    def test_user_url(self):
        url = reverse('info-list')
        self.assertEqual(url, '/user/info/')

    def test_history_url(self):
        url = reverse('history-list')
        self.assertEqual(url, '/user/history/')

    def test_star_url(self):
        url = reverse('star-list')
        self.assertEqual(url, '/user/star/')

    def test_progress_url(self):
        # 由于此处只是测试路由,写一个就足够,如果neep可以拼凑出来,那么(cet4/cet6)一般也不成问题
        url = reverse('progress', args=["1", "neep"])
        self.assertEqual(url, '/user/info/1/progress/neep/')
        # url=reverse('progress',args=["1","cet4"])
        # self.assertEqual(url, '/user/info/1/progress/cet4/')

    def test_review_recently_url(self):
        # 报错分析:(url 包含参数的时候,如果使用reverse()仅仅传入url_name,会报错,需要传入url_name和参数(args=[]))
        # django.urls.exceptions.NoReverseMatch: Reverse for 'review_recently' with no arguments not found.
        # 2 pattern(s) tried: ['user/info/(?P<pk>[0-9]+)/review/recently/\\Z', 'api/info/(?P<pk>[0-9]+)/review/recently/\\Z']
        url = reverse('review_recently', args=["1"])
        self.assertEqual(url, '/user/info/1/review/recently/')

    def test_review_list(self):
        url = reverse('review-list', args=["1", "neep"])
        self.assertEqual(url, '/user/info/1/review/neep/')
    def test_rank(self):
        url=reverse('rank',args=["1"])
        self.assertEqual(url,'/user/info/1/rank/')