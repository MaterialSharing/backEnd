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
from scoreImprover.serializer import NeepStudyModelSerializer
from scripts.numpyScripts import get_range_randoms
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

        random_words_pks = get_range_randoms(low=0, high=upper, contain_high=1, size=size)
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

    # def last_see(self,req):
    # neep_study_ob.exists(req.)
    def create_unique(self, req):
        data = {
            "id": 1,
            "last_see_datetime": "2022-05-13T10:26:40.857357Z",
            "familiarity": 1,
            "wid": 1
        }
        item = NeepStudy(**data)
