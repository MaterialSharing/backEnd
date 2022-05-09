import json

import django.http
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

# import ela.word.models
from rest_framework.viewsets import ModelViewSet

from .models import Word

import word.models
from .serializer import WordModleSerializer
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
    serializer_class = WordModleSerializer


class WordNotesModelViewSet(ModelViewSet):
    queryset = wnob.all()
    serializer_class = WordNotesModelSerializer


class Cet4WordsModelViewSet(ModelViewSet):
    queryset = c4ob.all()
    serializer_class = Cet4WordsReqModelSerializer


class Cet6WordsModelViewSet(ModelViewSet):
    queryset = c6ob.all()
    serializer_class = Cet6WordsReqModelSerializer


class NeepWordsModelViewSet(ModelViewSet):
    queryset = neepob.all()
    serializer_class = NeepWordsReqModelSerializer
