from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from scoreImprover.models import NeepStudy
from cxxulib import Randoms
from scoreImprover.serializer import NeepStudyModelSerializer, NeepStudyDetailModelSerializer
from word.models import WordNotes, Cet4WordsReq, Cet6WordsReq, NeepWordsReq
from word.serializer import NeepWordsReqModelSerializer, WordNotesModelSerializer, Cet4WordsReqModelSerializer, \
    Cet6WordsReqModelSerializer
from word.views import wob, c4ob, neepob
from word.serializer import WordModelSerializer


def index(request):
    return HttpResponse("Improver!")


# class Review(GenericAPIView,ListModelMixin):
#     queryset = wob.all()
#     serializer_class = WordModelSerializer
#
#     def get(self):
# class ListAPIView(mixins.ListModelMixin, GenericAPIView)
Res = Response


class Review(ListAPIView):
    queryset = c4ob.all()
    serializer_class = Cet4WordsReqModelSerializer

    def get(self, req, size=5):
        # size = 5
        if (size < 0):
            return Res({"msg": "requirement:size>=0! "})
        set = self.get_queryset()
        upper = set.count()

        random_words_pks = Randoms.Randoms.get_range_randoms(low=0, high=upper, contain_high=1, size=size)
        q_in = c4ob.filter(wordorder__in=random_words_pks)
        ser = self.serializer_class(instance=q_in, many=True)
        return Response(ser.data)

    # def list(self):
    #     pass
    # def get(self):
    #     queryset=


neep_study_ob = NeepStudy.objects


class NeepStudyModelViewSet(ModelViewSet):
    queryset = neep_study_ob.all()
    serializer_class = NeepStudyModelSerializer
    filter_fields = ["uid", "wid", "familiarity"]
    search_fields = filter_fields
    # def last_see(self,req):
    # neep_study_ob.exists(req.)
    """判断到底是要创建/修改学习记录,可以有前端完成,
    这里尝试后端处理(判断)"""

    def create_unique(self, req):
        # data = {
        #     # "id": 1,
        #     "last_see_datetime": "2022-05-13T10:26:40.857357Z",
        #     "familiarity": 1,
        #     "wid": 1,
        #     "uid": 1
        # }
        # 根据传入的req,提取其中的参数,查询数据库中是否已经有对应记录
        # 自动或者手动根据查询判断结果来增加或者修改一条学习记录
        # 我们要求前端需要传回至少包含uid&wid这两个字段
        wid = req.data.get("wid")
        uid = req.data.get("uid")
        queryset = neep_study_ob.filter(wid=wid) & neep_study_ob.filter(uid=uid)
        if queryset.count():
            instance = queryset[0]
            # print(f"@instance:{instance}")
            # print(instance)
            # print(f"@req.data{req.data}")
            ser = self.serializer_class(instance=instance, data=req.data)
            # if (instance):
        else:
            ser = self.serializer_class(data=req.data)

        ser.is_valid()
        ser.save()
        return Res(ser.data)
        # self.get_serializer_class()
        # self.update(req)
        # return Res(req.data, wid, uid)
        # return Res("...")
        # return Res({"msg":req.data})

        # item = NeepStudy(**data)

        # return self.create(req)

    def refresh(self, req):
        wid = req.data.get("wid")
        uid = req.data.get("uid")
        queryset = neep_study_ob.filter(wid=wid) & neep_study_ob.filter(uid=uid)
        if queryset.count():
            instance = queryset[0]
            ser = self.serializer_class(instance=instance, data=req.data)
            ser.is_valid()
            ser.save()
            return Res(ser.data)
            # todo 温习django的原生update(put)操作
            # return self.update(req, instance=instance)
        else:
            # ser = self.serializer_class(data=req.data)
            return self.create(req)
        # return Res(ser.data)


class NeepStudyDetailViewSet(ModelViewSet):
    queryset = neep_study_ob.all()
    serializer_class = NeepStudyDetailModelSerializer
    # pass
