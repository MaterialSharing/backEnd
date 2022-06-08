from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from scoreImprover.models import NeepStudy
from user.models import User
from user.views import uob
from word.models import NeepWordsReq
from word.views import neepob
from rest_framework.test import APIRequestFactory, APIClient


class ImproverViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.neep_list_url = reverse('improver:neep-list')
        self.neep_detail1_url = reverse('improver:neep-detail', args=["1"])
        # 由于NeepStudy中的user&wid字段是外键字段,所以需要传递实例
        # 如果使用DRF序列化器,不一定
        self.study_neep1 = NeepStudy.objects.create(,

        # self.study_neep1 = NeepStudy.objects.create(
        #     familiarity=4, user=1, wid=1
        # )

    def test_neep_create(self):
        # 测试post的时候,如果使用 --keepdb 可能会有旧数据影响
        # pmg test scoreImprover.tests.test_views.ImproverViewTestCase
        url = reverse('improver:neep-list')
        self.assertEqual(url, '/improver/neep/')
        print("@url", url)
        # 预览测试!
        # 注意user&wid的数值,需要和下面创建的外键对象数量相匹配
        study_neep0 = {
            "familiarity": 4,
            "user": 1,
            "wid": 1
        }
        # study_neep0 = {
        #     "familiarity": 4,
        #     "user": 11,
        #     "wid": 1
        # }
        """错误实例"""

        # @w[2, 'test']
        # @u[2, 'test', 0, '1970-01-01', '4', datetime.date(2022, 5, 21)]
        # @response
        #
        # {'user': [ErrorDetail(string='Invalid pk "11" - object does not exist.', code='does_not_exist')]}
        # 400
        """ 符合要求的user&wid"""
        # 根据外键要求,创建用户/考纲单词对象
        # 注意,单词是考纲模型中的对象,而不是词典那里的.
        user_d = {
            "name": "test",
        }
        word_d = {
            "spelling": "test",
        }
        w = neepob.create(,
        print("@w", w)
        u = uob.create(,
        print("@u", u)

        response = self.client.post(url, study_neep0)
        # response1 = self.client.post(url, self.study_neep1)
        # response = client.post(url, study)
        print("@response", response.data, response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # factory = APIRequestFactory()
        # req = factory.post(url, study)
        # print(req)
