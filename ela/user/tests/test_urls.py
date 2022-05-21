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
        url = reverse('progress',args=["1","neep"])
        self.assertEqual(url, '/user/info/1/progress/neep/')
        # url=reverse('progress',args=["1","cet4"])
        # self.assertEqual(url, '/user/info/1/progress/cet4/')
