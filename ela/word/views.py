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
from rest_framework import filters
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# from user.views import Res

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
                "phnetic": word.phonetic,
                "explains": word.explains
            })
        # print(word)
        # print(Word.objects.get(spelling=word))
        # word_list=query_set
        #     json_dumps_params可以设置中文编码使得其在浏览器中可以正确显示(不排斥非ascii编码)
        return django.http.JsonResponse(word_list, safe=False, json_dumps_params={"ensure_ascii": False})


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

    # search_fields = ['$spelling', 'plurality', 'thirdpp', 'presetn_participle', 'past_tense', 'past_participle']

    # @action(method=["get"],detail=False)
    def explain(self, req, spelling):
        word = self.get_queryset().get(spelling=spelling)
        ser = self.serializer_class(instance=word)
        return Res(ser.data)


class WordMatcherViewSet(ModelViewSet):
    """ 模糊匹配数据库"""
    queryset = wmob.all()
    serializer_class = WordMatcherModelSerializer
    filter_fields = ['spelling', 'char_set']

    def fuzzy_match(self, req, spelling):
        # spelling_chars = "".join(list(set(spelling)).sort())
        spelling_char_list = list(set(spelling))
        spelling_char_list.sort()
        spelling_char_set = set(spelling_char_list)
        spelling_char_set_str = "".join(spelling_char_set)
        spelling_char_set_len = len(spelling_char_set)
        # print("@spelling_chars:", spelling_char_set_str)

        # print(spelling_chars)
        spelling_len = len(spelling)
        left_len = spelling_len * 0.70
        # right_len = spelling_len * 1.25
        right_len = spelling_len * 1.25
        if spelling_len >= 4:
            right_len = spelling_len * 2

        # 模糊匹配
        # queryset = self.get_queryset().filter(spelling__length__gte=left_len) & self.get_queryset().filter(
        #     spelling__length__lte=right_len) & self.queryset.filter(char_set__contains=spelling_chars)
        """debug code:"""
        # queryset_len = wmob.filter(spelling__length__gte=left_len) & wmob.filter(
        #     spelling__length__lte=right_len)
        # print("@queryset_len:", queryset_len )
        # querset_contains =wmob.filter(char_set__contains=spelling_chars)
        # print("@querset_contains:", querset_contains)
        """限制单词长度"""
        queryset = self.queryset.filter(spelling__length__gte=left_len) & self.queryset.filter(
            spelling__length__lte=right_len)
        # 匹配开头(严格模式)(可以额外设置变量,追加if)
        # print(queryset)
        # 匹配发音:mysql中有一个soundx函数,
        queryset = queryset.filter(spelling__startswith=spelling[:1])
        """限制单词字符集规模的差异"""
        # 10:14(5:7);
        # 10:16(5:8);
        queryset = queryset.filter(char_set__length__lte=1.25 * spelling_char_set_len)
        # 3:5;
        # 4:5
        queryset = queryset.filter(char_set__length__gte=0.6 * spelling_char_set_len)

        """匹配字符组成(最后一步)"""
        # 方案0:使用icontains函数来匹配(无法匹配到替换了个别字母的形近词!
        ## 可以引入随机剔除字符操作
        # 方案1:双向包含(或运算)(比上衣种情况稍好,但还是无法满足需求)
        # 方案2:差集(限制差集中的元素个数)(容错个别字母(种类)的不同)
        # queryin = queryset.filter(char_set__in=spelling_chars)
        # print("@queryin:", queryin)
        # queryset = queryset.filter(Q(char_set__contains=spelling_chars) | Q(char_set__in=spelling_chars))
        items = []
        for item in queryset:
            item_char_set_len = len(item.char_set)
            item_spelling_len = len(item.spelling)
            intersection = set(item.char_set) & set(spelling_char_set)
            intersection_len = len(intersection)
            # if (item.spelling == "dad"):
            #     print("dad", diff, len(diff), item, spelling_chars_len * 0.5)
            #     # print()
            if (spelling_len >= 5):
                if (intersection_len >= spelling_char_set_len * 0.8 and intersection_len >= item_char_set_len * 0.8):
                    # if (item.spelling == "dad"):
                    # print(item, diff)
                    items.append(item)
            elif (intersection == spelling_char_set):
                # else:
                print("@intersection", intersection)
                print("@spelling_char_set", spelling_char_set)
                print(item, intersection, spelling_char_set_len)
                if (item_spelling_len == spelling_len):
                    items.append(item)

        # print(queryset)
        print(len(items))
        return Res(self.serializer_class(instance=items, many=True).data)
        return Res(self.serializer_class(instance=queryset, many=True).data)


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
        if (examtype == "6"):
            queryset = c6ob
        elif (examtype == "8"):
            queryset = neepob
        sum = queryset.all().count()
        print(sum)
        # return Res({examtype: queryset.all().count()})
        return Res({examtype: sum})
