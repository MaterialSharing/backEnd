from rest_framework.response import Response

from scoreImprover.models import Cet4Study, Cet6Study, NeepStudy
from word.serializer import Cet4WordsReqModelSerializer, Cet6WordsReqModelSerializer, NeepWordsReqModelSerializer
from word.views import c4ob, c6ob, neepob

Res = Response

cet4_study_ob = Cet4Study.objects
cet6_study_ob = Cet6Study.objects
neep_study_ob = NeepStudy.objects


class QuerysetDispatcher:
    """ to use these methods,you'd instantiate the QueryDispatcher first,
    then the `self` parameter could be passed to the methods automatically.
    just like :
    queryDispatcher=QueryDispatcher()#after that ,could you use queryDispatcher.method()
    """

    def get_queryset_study(self, examtype="4"):
        """使用的时候注意examtype 关键字参数不要以位置参数的形式传递!!!"""
        print("@examtype:", examtype)
        queryset = cet4_study_ob
        if (examtype == "cet6"):
            queryset = cet6_study_ob
        elif (examtype == "neep"):
            queryset = neep_study_ob
        # sum = queryset.all().count()
        # print(sum)
        print("@dispatcher:queryset_study:", queryset)
        return queryset

    def get_queryset_reqs(self, examtype="4"):
        # 考纲表manager
        queryset = c4ob
        if (examtype == "cet6"):
            queryset = c6ob
        elif (examtype == "neep"):
            queryset = neepob
        # sum = queryset.all().count()
        # print(sum)
        print("@dispatcher:queryset_reqs:", queryset)
        return queryset

    def get_serializer_class_reqs(self, examtype="4"):
        ser = Cet4WordsReqModelSerializer
        if (examtype == "cet6"):
            ser = Cet6WordsReqModelSerializer
        elif (examtype == "neep"):
            ser = NeepWordsReqModelSerializer
        print("@dispatcher:", ser)
        return ser
