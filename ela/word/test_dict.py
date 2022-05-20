from django.test import TestCase
from django.test import Client
from django.urls import reverse

# AssertTrue, AssertFalse, AssertEqual 是 unittest 提供的标准断言。框架中还有其他标准断言，还有 Django 特定的断言，来测试视图是否重定向（assertRedirects），或测试是否已使用特定模板（assertTemplateUsed）等。
#
# 注意：您通常不应在测试中包含print() 函数，
# 如上所示。我们这样做，只是为了让您可以看到在控制台中，调用设置功能的顺序（在下一节中）。

# 显示更多测试信息
# 如果您想获得有关测试运行的更多信息，可以更改详细程度。例如，要列出测试成功和失败（以及有关如何设置测试数据库的大量信息），您可以将详细程度设置为 “2”，如下所示：
# python3 manage.py test --verbosity 2
# 允许的详细级别为 0, 1 ,2 和 3，默认值为 “1".

# 视图
# 为了验证我们的视图行为，我们使用 Django 的测试客户端。
# 这个类，就像一个虚拟的Web浏览器，我们可以使用它，来模拟URL上的GET和POST请求，并观察响应。我们几乎可以看到，关于响应的所有内容，从低层级的 HTTP（结果标头和状态代码），到我们用来呈现HTML的模板，
# 以及我们传递给它的上下文数据。我们还可以看到重定向链（如果有的话），并在每一步检查URL，和状态代码。这允许我们验证每个视图，是否正在执行预期的操作.
from rest_framework.test import APIClient

# client=Client()
# drf client(Extends Django's existing Client class.)
client = APIClient()


class DictTestCase(TestCase):
    # setUpTestData()
    # 用于类级别设置，在测试运行开始的时侯，会调用一次。您可以使用它来创建在任何测试方法中，都不会修改或更改的对象。
    # setUp()
    # 在每个测试函数之前被调用，以设置可能被测试修改的任何对象（每个测试函数，都将获得这些对象的 “新” 版本）。
    def test_no_explain(self):
        # print("@@@@@@")
        # 您可以在测试中做一些打印操作,但是这不被建议
        # res = self.client.get(reverse("word:dict"))
        # res = self.client.get('http://127.0.0.1:8000/word/dict/apple/')
        # self.assertEqual(res.status_code, 200)
        pass

    def test_reverse(self):
        dict_url = reverse('dict_spelling', args=['apple'])
        self.assertEqual(dict_url, '/word/dict/apple/')
        res = self.client.get(dict_url)
        res=self.client.get('/word/dict/apple')
        res=client.get('/word/dict/apple/')

        # self.assertEqual(res.status_code,200)
        print('@type_res:', type(res))
        # print("@res.data:",res._)
        print("@res.content", res.content.decode('utf-8'))

        # dict_list_url = reverse('/word/dict')
        dict_list_url = reverse('dict_drf-list')
        # 判断解析的路径是否正确
        self.assertEqual(dict_list_url, '/word/dict/')
        # 查看列表
        res = self.client.get(dict_list_url+"1")
        print('@type_res_list:', type(res))
        # print("@res.data:",res._)
        print("@res.content_list", res.content.decode('utf-8'))

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        # AssertionError: False is not true
        # self.assertTrue(False)
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)


class FuzzyTestCase(TestCase):
    # 局部测试本类中的所有测试函数(使用点式路径来指定)
    # pmg test  word.test_dict.FuzzyTestCase --keepdb
    # Get second page and confirm it has (exactly) remaining 3 items
    # resp = self.client.get(reverse('authors') + '?page=2')
    def test_spelling_start_with(self):
        spelling_start_url = reverse('fuzzy', args=['decay', "0"])
        res = self.client.get(spelling_start_url)
        print("@spelling_start_url:", spelling_start_url)
        # http://127.0.0.1:8000/word/fuzzy/decay/0/
        self.assertEqual(res.status_code, 200)
        # self.assertContains(res,"de")
        # res.content.decode('utf-8')
        print("@res.data:", res.data)
    # def test_contain_url(self):
    #     # url query参数是字符串(使用字典模拟query参数)
    #     contain_url = reverse('fuzzy')
    #     print("@contain_url:",contain_url)
