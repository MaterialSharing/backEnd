# from unittest import TestCase
from django.test import TestCase
from django.urls import reverse, resolve

from cxxulib.printer import print1
from word import views
from word.views import wob, IndexAPIView


#

# 测试本类的命令
# pmg test word.tests.test_urls.DictTestCase  --keepdb
class DictTestCase(TestCase):
    # setUpTestData()
    # 用于类级别设置，在测试运行开始的时侯，会调用一次。您可以使用它来创建在任何测试方法中，都不会修改或更改的对象。
    # setUp()
    # 在每个测试函数之前被调用，以设置可能被测试修改的任何对象（每个测试函数，都将获得这些对象的 “新” 版本）。
    def test_demo(self):
        # 检查基本的捕获DRF::Response对象是否可行.
        # word = create_word()
        # word = create_word()
        # print(word)

        test_url = reverse('test')
        resolved_url = resolve(test_url)
        # url_name,route,view,
        view, args, kwargs = resolve(test_url)
        # print("@view:", view)
        # print("@args:", args)
        # print("@kwargs:", kwargs)
        print("@resolve_url:", resolved_url)
        # @resolve_url: ResolverMatch(
        # func=word.views.WordDemoTestAPIView, args=(), kwargs={}, url_name='test', app_names=[], namespaces=[], route='word/test/')
        # print("@url_name,route:", url_name,route)
        print("@resolved_url.func:", resolved_url.func)
        # 相比于客户端client发送请求并判断返回值,这里用resolve判断视图函数,更加具体.
        # 不过大多数情况下,使用self.client.get()足够应付路由的有效性!
        # <function View.as_view.<locals>.view at 0x0000015CAF752440> # 实际视图函数
        # 注意到,这里的视图函数类型是<function>一个函数.
        # 而<class 'word.views.WordDemoTestAPIView'>是一个类.所以下方的断言是不可行的.
        # self.assertEqual(resolved_url.func, views.WordDemoTestAPIView)
        # 现在,我们尝试访问函数对象下的view_class属性,并判断是否为WordDemoTestAPIView.
        print("@resolved_url.func.view_class:", resolved_url.func.view_class)
        # 通过查看属性,我们捕获到了<function>对象中的属性view_class.(应该是我们需要的)
        # print1("@dir(resolved_url.func):", dir(resolved_url.func))
        self.assertEqual(resolved_url.func.view_class, views.WordDemoTestAPIView)
        self.assertEqual(resolved_url.func.view_class.get, views.WordDemoTestAPIView.get)

        # print("@test_url", test_url)
        # res = self.client.get(test_url)
        # # print("@res.type:", type(res.data))
        # # print("@res", res)
        # # print("@res.data", res.data)

    def test_dict(self):
        # 被测试路由如下:
        #    # <str:spelling>将被转换为正则: ?P<spelling>[^/]+)/\\Z
        #     path('dict/<str:spelling>/', views.WordModelViewSet.as_view({
        #         "get": "dict"
        #     }), name='dict_spelling'),
        # 我们这里有一个url参数,它是一个字符串,它的名字是spelling.
        url = reverse('dict_spelling', args=['hello'])
        self.assertEqual(url, '/word/dict/hello/')
        # 由于我们没有为临时数据库创建数据,所以这里仅仅测试该路由pattern是否可以解析传递进来的url!
        resolve_url = resolve(url)
        print("@resolve_url:", resolve_url)
        self.assertEqual(resolve_url.route, 'word/dict/<str:spelling>/')
        print("@resolve_url.func:", resolve_url.func)
        # print("@resolve_url.funcs:", dir(resolve_url.func))
        # print("@resolve_url.funcs:", resolve_url.func.cls)
        """视图功能的测试"""
        # client.get()一般用户测试视图(函数);需要手动创建测试数据;并且手动编写写入数据库的语句(create),否则访问的是空数据/404
        # 例如
        # word1 = {
        #     "spelling": 'hello',
        #     "explains": '你好!'
        #
        # }
        # wob.create(**word1)
        #
        # res = self.client.get(url)
        # self.assertEqual(res.status_code, 200)

    def test_fuzzy_simple(self):
        #   path('fuzzy/<str:spelling>/', views.WordMatcherViewSet.as_view({
        #         "get": "fuzzy_match_simple"
        #     })),
        url = reverse('fuzzy_match_simple', args=['hello'])
        self.assertEqual(url, '/word/fuzzy/hello/')

    def test_fuzzy(self):
        #  path('fuzzy/<str:spelling>/<int:start_with>/', views.WordMatcherViewSet.as_view({
        #         "get": "fuzzy_match"
        #     }), name="fuzzy"),
        url = reverse('fuzzy', args=['hello', "1"])
        self.assertEqual(url, '/word/fuzzy/hello/1/')
        # query_url = url + "?end_with=2&contain=1"
        # res_matcher = resolve(query_url)
        # self.assertEqual(res_matcher.url_name, 'fuzzy')

    def test_sum(self):
        url = reverse('sum', args=["cet4"])
        self.assertEqual(url, '/word/sum/cet4/')
        url = reverse('sum', args=["cet6"])
        self.assertEqual(url, '/word/sum/cet6/')
        url = reverse('sum', args=["neep"])
        self.assertEqual(url, '/word/sum/neep/')
    def test_dict_drf(self):
        url=reverse('dict-list')
        self.assertEqual(url, '/word/dict/')
    def test_cet4(self):
        url=reverse('cet4-list')
        self.assertEqual(url, '/word/cet4/')
    def test_cet6(self):
        url=reverse('cet6-list')
        self.assertEqual(url, '/word/cet6/')
    def test_neep(self):
        url=reverse('neep-list')
        self.assertEqual(url, '/word/neep/')
    def test_note(self):
        url=reverse('note-list')
        self.assertEqual(url, '/word/note/')