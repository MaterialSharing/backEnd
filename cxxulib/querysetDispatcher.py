from rest_framework.response import Response

from scoreImprover.models import Cet4Study, Cet6Study, NeepStudy
from scoreImprover.serializer import Cet4StudyModelSerializer, Cet6StudyModelSerializer, NeepStudyModelSerializer
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
    req_qs_d = {
        'cet4': c4ob,
        'cet6': c6ob,
        'neep': neepob
    }
    req_ser_d = {
        'cet4': Cet4WordsReqModelSerializer,
        'cet6': Cet6WordsReqModelSerializer,
        'neep': NeepWordsReqModelSerializer
    }
    study_qs_d = {
        "cet4": cet4_study_ob,
        "cet6": cet6_study_ob,
        "neep": neep_study_ob,
    }
    study_ser_d = {"cet4": Cet4StudyModelSerializer,
                   "cet6": Cet6StudyModelSerializer,
                   "neep": NeepStudyModelSerializer}

    # 用户传入的url中examtype可能是cet4,cet6,neep,之外的值,如果不处理,会导致报错
    # 您可以编写相关的类来处理这个问题,或者在这里做一个判断设置一个默认值(提醒调用者)
    # @staticmethod
    # 静态方法没有self参数(或者类似@类方法的cls参数)，所以不需要实例化
    @classmethod
    def get_queryset_study(self, examtype="4"):
        """使用的时候注意examtype 关键字参数不要以位置参数的形式传递!!!"""

        queryset=self.study_qs_d[examtype]
        return queryset

    @classmethod
    def get_queryset_req(self, examtype="4"):

        queryset=self.req_qs_d[examtype]
        return queryset

    @classmethod
    def get_serializer_class_req(self, examtype="4"):
        ser=self.req_ser_d[examtype]
        # ser = Cet4WordsReqModelSerializer
        # if (examtype == "cet6"):
        #     ser = Cet6WordsReqModelSerializer
        # elif (examtype == "neep"):
        #     ser = NeepWordsReqModelSerializer
        # print("@dispatcher:", ser)
        return ser

    @classmethod
    def get_serializer_class_study(self, examtype="4"):

        # 建立字典,提高复用性和简化代码!
        # ser = Cet4StudyModelSerializer
        # if (examtype == "cet6"):
        #     ser = Cet6StudyModelSerializer
        # elif (examtype == "neep"):
        #     ser = NeepStudyModelSerializer
        # print("@dispatcher:", ser)
        ser = self.study_ser_d[examtype]
        return ser
