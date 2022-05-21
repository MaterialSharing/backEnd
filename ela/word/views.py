import json
from warnings import filters

import django.http
from deprecated.classic import deprecated
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

# import ela.word.models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import filters, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# from user.views import Res
from .paginations import DIYPagination
from .models import Word

import word.models
from .serializer import WordModelSerializer, WordMatcherModelSerializer
from word.models import WordNotes, Cet4WordsReq, Cet6WordsReq, NeepWordsReq, WordMatcher
from word.serializer import NeepWordsReqModelSerializer, WordNotesModelSerializer, Cet4WordsReqModelSerializer, \
    Cet6WordsReqModelSerializer

wob = Word.objects
wmob = WordMatcher.objects

wnob = WordNotes.objects
c4ob = Cet4WordsReq.objects
c6ob = Cet6WordsReq.objects
neepob = NeepWordsReq.objects

Res = Response


def index(request):
    return HttpResponse("Words!")


class IndexAPIView(APIView):
    def get(self, request):
        5 / 0
        # ????
        return Response("Words!_drf")


@deprecated
class WordAPIView(View):
    def get(self, request, word="apply"):
        # query_set= Word.objects.all()[:10]

        # word_list=[]
        # for word in query_set:
        #     word_list.append({
        #         "spelling":word.spelling,
        #         "phnetic":word.phonetic,
        #         "explains":word.explains
        #     })
        # queue_set=Word.get(sepelling=word)

        query_set = Word.objects.filter(spelling__exact=word)
        print(word)
        word_list = []
        for word in query_set:
            print(word)
            word_list.append({
                "spelling": word.spelling,
                "phonetic": word.phonetic,
                "explains": word.explains
            })
        # print(word)
        # print(Word.objects.get(spelling=word))
        # word_list=query_set
        #     json_dumps_params可以设置中文编码使得其在浏览器中可以正确显示(不排斥非ascii编码)
        return django.http.JsonResponse(word_list, safe=False, json_dumps_params={"ensure_ascii": False})


class WordDemoTestAPIView(APIView):

    def get(self, req):
        words = Word.objects.all()[:1]
        # data=WordModelSerializer(words, many=True).data
        # data_str=str(data)[:10]
        word1=words[0]
        data1={
            "spelling":word1.spelling,
            "phnetic":word1.phonetic,
            "explains":word1.explains
        }
        print(data1)
        # return Res("WordDemoTestView@@@!"+data1)
        return Res(data1)
        # return Res(str(data))
class WordModelViewSet(ModelViewSet):
    queryset = wob.all()
    serializer_class = WordModelSerializer
    # 过滤+排序,统一配置(要么都局部/要么都在setting中全局配置,才可以同是生效
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # http://127.0.0.1:8000/word/dict/?ordering=-spelling
    filter_fields = ['spelling', 'wid', 'plurality', 'thirdpp']
    # 使用单引号!!
    # search_fields = ['$spelling']
    search_fields = ['$spelling', 'plurality', 'thirdpp', 'present_participle', 'past_tense', 'past_participle']

    ordering_fields = ['spelling', 'id']
    pagination_class = DIYPagination

    # search_fields = ['$spelling', 'plurality', 'thirdpp', 'presetn_participle', 'past_tense', 'past_participle']

    # @action(method=["get"],detail=False)
    def dict(self, req, spelling):
        # word = self.get_queryset().get(spelling=spelling)
        word_queryset = get_object_or_404(wob, spelling=spelling)
        # 使用get如果查询无果,会抛出异常! 使用filter如果查询无果,返回空集合
        # word_queryset = self.get_queryset().filter(spelling=spelling)
        # if (len(word_queryset) == 0):
        #     return Res(f"sorry,there is no explain for the word:{spelling},try fuzzy match api? /word/fuzzy/{spelling}",
        #                status=status.HTTP_404_NOT_FOUND)
        # ser = self.serializer_class(instance=word_queryset,many=True)
        ser = self.serializer_class(instance=word_queryset)
        return Res(ser.data)
        # .renderer_context({"test_moreinf":"good!!!"})


class WordMatcherViewSet(ModelViewSet):
    """ 模糊匹配数据库"""
    queryset = wmob.all()
    serializer_class = WordMatcherModelSerializer
    # 使用coreapi可以自动生成文档,同时会检查一些错误(比如视图类于被更改的模型字段引用不匹配)
    filter_fields = ['spelling', 'char_set_str']
    search_fields = ['$spelling', 'char_set_str']

    def fuzzy_match(self, req, spelling, start_with=0, contain=0):
        """
        :param req:
        :type req:
        :param spelling:
        :type spelling:
        :param start_with:匹配开头的字符串长度 (default: {0},表示没有被强制规定)
        :type start_with:
        :return:
        :rtype: Response
        """
        params = req.query_params
        print("@params", params, type(params))
        contain = params.get("contain", 0)
        end_with = params.get("end_with", 0)
        if (contain == ""):
            contain = 0
        if (end_with == ""):
            end_with = 0
        contain = int(contain)
        end_with = int(end_with)

        # print("@contain:", contain)
        spelling_len = len(spelling)
        # 根据模糊拼写的长度,选择一个较为合适的start_with
        if (start_with == 0):
            # 没有被强制设值
            # 启用内部判断取值
            if (spelling_len > 4):
                start_with = 2
            else:
                start_with = 1
        # 获得模糊拼写的字母集合
        spelling_char_set = set(spelling)
        # 获取模糊拼写的字母集列表(字母集合去重后转换为列表)
        spelling_char_list = list(spelling_char_set)
        # 对字母集合转成的列表进行排序
        spelling_char_list.sort()
        # 获得有序的字符集字符串
        spelling_char_set_str = "".join(spelling_char_list)
        spelling_char_set_len = len(spelling_char_set)
        # print("@spelling_chars:", spelling_char_set_str)
        # 定义匹配的单词的长度范围
        left_len = spelling_len * 0.70
        # right_len = spelling_len * 1.25
        right_len = spelling_len * 1.4
        if spelling_len >= 4:
            right_len = spelling_len * 2

        # 模糊匹配
        # queryset = self.get_queryset().filter(spelling__length__gte=left_len) & self.get_queryset().filter(
        #     spelling__length__lte=right_len) & self.queryset.filter(char_set__contains=spelling_chars)

        """限制单词长度"""
        queryset = self.queryset.filter(spelling__length__gte=left_len) & self.queryset.filter(
            spelling__length__lte=right_len)
        # 是否要求模糊输入的拼写字符集是候选词的子集(强制)
        if (contain):
            # 基于候选拼写的特征字符集
            # 这里char_set是字符串
            # 候选词的字符集作为全集(contains作用于字符串之间的判断)
            queryset = queryset.filter(char_set_str__contains=spelling_char_set_str)

        if (end_with):
            print("@end_with:", end_with)
            # 基于完整的候选拼写
            queryset = queryset.filter(spelling__endswith=spelling[-int(end_with):])
        # 匹配开头(严格模式)(可以额外设置变量,追加if)
        # print(queryset)
        # 匹配发音:mysql中有一个soundx函数,
        # 匹配开头的start_with个字符
        queryset = queryset.filter(spelling__startswith=spelling[:start_with])
        """限制单词字符集规模的差异"""
        # 10:14(5:7);
        # 10:16(5:8);
        queryset = queryset.filter(char_set_str__length__lte=1.25 * spelling_char_set_len)
        # 3:5;
        # 4:5
        queryset = queryset.filter(char_set_str__length__gte=0.6 * spelling_char_set_len)
        # 此时如果是contain=1,那么就直接返回结果了
        if (contain):
            print(queryset)
            return Res(self.serializer_class(instance=queryset, many=True).data)
        """匹配字符组成(最后一步)"""
        # 方案0:使用icontains函数来匹配(无法匹配到替换了个别字母的形近词!
        ## 可以引入随机剔除字符操作
        # 方案1:双向包含(或运算)(比上衣种情况稍好,但还是无法满足需求)
        # 方案2:差集(限制差集中的元素个数)(容错个别字母(种类)的不同)
        # queryin = queryset.filter(char_set_str__in=spelling_chars)
        # print("@queryin:", queryin)
        # queryset = queryset.filter(Q(char_set_str__contains=spelling_chars) | Q(char_set_str__in=spelling_chars))

        items = []
        for item in queryset:
            intersection = set(item.char_set_str) & set(spelling_char_set)
            intersection_len = len(intersection)
            item_char_set = set(item.char_set_str)
            item_char_set_len = len(item_char_set)
            item_spelling_len = len(item.spelling)
            # if (item.spelling == "dad"):
            #     print("dad", diff, len(diff), item, spelling_chars_len * 0.5)
            #     # print()
            # if (contain):
            #     if (item_char_set.issubset(spelling_char_set) or spelling_char_set.issubset(item_char_set)):
            #         items.append(item)

            if (spelling_len >= 5):
                if (intersection_len > spelling_char_set_len * 0.7 and intersection_len >= item_char_set_len * 0.8):
                    # if (item.spelling == "dad"):
                    # print(item, diff)
                    items.append(item)
            elif (intersection == spelling_char_set):
                #     长度小于5的输入,我们只需要检查是否包含全部字符即可
                # else:
                print("@intersection", intersection)
                print("@spelling_char_set", spelling_char_set)
                print(item, intersection, spelling_char_set_len)
                if (item_spelling_len == spelling_len):
                    items.append(item)

        # print(queryset)
        items.sort(key=lambda x: x.spelling)
        print(len(items))
        return Res(self.serializer_class(instance=items, many=True).data)
        # return Res(self.serializer_class(instance=queryset, many=True).data)

    def fuzzy_match_simple(self, req, spelling):
        return self.fuzzy_match(req, spelling)


class WordNotesModelViewSet(ModelViewSet):
    queryset = wnob.all()
    serializer_class = WordNotesModelSerializer

    #     指定需要开放的可排序/可过滤字段
    filter_fields = ["spelling", "difficulty_rate", "uid"]
    ordering_fields = ['spelling', 'uid']


class Cet4WordsModelViewSet(ModelViewSet):
    queryset = c4ob.all()
    serializer_class = Cet4WordsReqModelSerializer
    # 过滤/搜索/排序/分页
    ## individual filter_backends config(local for current View)
    ### 局部单独配置会覆盖全局变量
    # filter_backends = [filters.SearchFilter,DjangoFilterBackend,OrderingFilter ]
    # filter_backends = [filters.SearchFilter]
    # 过滤
    ##基本过滤
    filter_fields = ['spelling', 'wordorder']  # 指定模型字段,作为url参数名
    ##基于文本字段的过滤
    ### 点击Filter按钮,可以弹出Search框,该api默认提供类似contain的效果
    """
    The search behavior may be restricted by prepending various characters to the search_fields.
    '^' Starts-with search.
    '=' Exact matches.
    '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    '$' Regex search.
    """
    ####  正则搜索:测试连接:
    """     http://127.0.0.1:8000/word/cet4/?search=s.*p.*
    """
    search_fields = ['$spelling']
    # http://127.0.0.1:8000/word/cet4/?ordering=-spelling
    # 排序
    ordering_fields = ['spelling', 'wordorder']


class Cet6WordsModelViewSet(ModelViewSet):
    queryset = c6ob.all()
    serializer_class = Cet6WordsReqModelSerializer


class NeepWordsModelViewSet(ModelViewSet):
    queryset = neepob.all()
    serializer_class = NeepWordsReqModelSerializer


# 逻辑类
class WordSumModelViewSet(APIView):
    # queryset_c4 = c4ob.all()

    def get(self, req, examtype):
        queryset = c4ob
        if (examtype == "cet6"):
            queryset = c6ob
        elif (examtype == "neep"):
            queryset = neepob
        sum = queryset.all().count()
        print(sum)
        # return Res({examtype: queryset.all().count()})
        return Res({"examtype": examtype, "sum": sum})
