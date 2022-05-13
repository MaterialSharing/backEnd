import json
from warnings import filters

import django.http
from deprecated.classic import deprecated
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

# import ela.word.models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Word

import word.models
from .serializer import WordModelSerializer
from word.models import WordNotes, Cet4WordsReq, Cet6WordsReq, NeepWordsReq
from word.serializer import NeepWordsReqModelSerializer, WordNotesModelSerializer, Cet4WordsReqModelSerializer, \
    Cet6WordsReqModelSerializer

wob = Word.objects
wnob = WordNotes.objects
c4ob = Cet4WordsReq.objects
c6ob = Cet6WordsReq.objects
neepob = NeepWordsReq.objects


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
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # http://127.0.0.1:8000/word/dict/?ordering=-spelling
    filter_fields = ['spelling', 'wid', 'plurality', 'thirdpp']
    ordering_fields = ['spelling', 'id']
    # @action(method=["get"],detail=False)
    # def


class WordNotesModelViewSet(ModelViewSet):
    queryset = wnob.all()
    serializer_class = WordNotesModelSerializer

    #     指定需要开放的可排序/可过滤字段
    filter_fields = ["spelling", "difficulty_rate", "uid"]
    search_fields = ['$spelling']
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
