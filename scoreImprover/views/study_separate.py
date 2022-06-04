from collections import OrderedDict
from datetime import timedelta

from deprecated.classic import deprecated
from django.db.models import F
from django.http import HttpResponse
# Create your views here.
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from cxxulib.querysetDispatcher import QuerysetDispatcher
from cxxulib.randoms import Randoms
from cxxulib.static_values import neep_study_ob, Res, cet4_study_ob, cet6_study_ob
from scoreImprover.models import NeepStudy, Cet4Study, Cet6Study, Study
from scoreImprover.serializer import NeepStudyModelSerializer, NeepStudyDetailModelSerializer, Cet4StudyModelSerializer, \
    Cet6StudyModelSerializer


def index(request):
    return HttpResponse("Improver!")


# class Review(GenericAPIView,ListModelMixin):
#     queryset = wob.all()
#     serializer_class = WordModelSerializer
#
#     def get(self):
# class ListAPIView(mixins.ListModelMixin, GenericAPIView)
# Res = Response
#
# cet4_study_ob = Cet4Study.objects
# cet6_study_ob = Cet6Study.objects
# neep_study_ob = NeepStudy.objects
# study_ob = Study.objects


class NeepStudyModelViewSet(ModelViewSet):
    queryset = neep_study_ob.all()
    serializer_class = NeepStudyModelSerializer
    filter_fields = ["user", "wid", "familiarity"]
    search_fields = filter_fields
    # def last_see(self,req):
    # neep_study_ob.exists(req.)
    """判断到底是要创建/修改学习记录,可以有前端完成,
    这里尝试后端处理(判断)"""

    @deprecated
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

    @deprecated("the more Generic method is in the RefresherModelViewSet")
    def refresh(self, req):
        # wid&wid_id
        # uid&uid_id
        wid = req.data.get("wid_id")
        user = req.data.get("user_id")
        print("req.data", req.data)

        queryset = neep_study_ob.filter(wid=wid) & neep_study_ob.filter(user=user)
        print("@queryset", queryset)

        # if queryset.count():
        #     instance = queryset[0]
        #     ser = self.serializer_class(instance=instance, data=req.data)
        #     ser.is_valid()
        #     ser.save()
        #     return Res(ser.data)
        # todo 温习django的原生update(put)操作
        # return self.update(req, instance=instance)
        if queryset.count():  # 原生方案
            instance = queryset[0]
            # 执行一次幂等操作,使得其可以触发时间更新操作!
            # instance.wid += 0#error:外键类型wid是属于Word模型实例,而不是整型
            # 单纯的对一个未修改的对象执行一次save()操作,也可以触发modified 条件,以便于自动更新时间字段(auto_now=True)
            instance.save()
            # ser = self.serializer_class(instance=instance, data=req.data)
            ser = self.serializer_class(instance=instance)
            # 序列化需要被更新的对象
            data = ser.data
            return Res(data, status=status.HTTP_201_CREATED)

            # drf 方案
            # 先通过get_serializer()拿到构造函数器(对象),将构造器对象作为函数进行调用,
            # 传入data=req.data;
            # ser=self.get_serializer()(data=req.data)
            # ser.save()

        else:
            # ser = self.serializer_class(data=req.data)
            # drf CreateModelMixin.create()
            return self.create(req)
        # return Res(ser.data)

    @deprecated
    def recently(self, req, days):
        queryset = neep_study_ob.filter(last_see_datetime__gte=timezone.now() - timedelta(days=float(days)))
        return Res(self.serializer_class(instance=queryset, many=True).data)

    # def recently_unitable(self, req, unit, value):
    #     value = float(value)
    #     # 只需要使用字典打包以下关键字参数
    #     d = {unit: value}
    #     delta = timedelta(**d)
    #     # delta = timedelta({unit: value})
    #
    #     # 您不需要如下的负责判断
    #     # if (unit == 'days'):
    #     #     delta = timedelta(days=value)
    #     # elif (unit == 'hours'):
    #     #     delta = timedelta(hours=value)
    #     # else:
    #     #     print("unit的取值是hours或者days!")
    #     queryset = neep_study_ob.filter(last_see_datetime__gte=timezone.now() - delta)
    #
    #     return Res(self.serializer_class(instance=queryset, many=True).data)

    @deprecated("为了通用性,已将功能转移到RandomInspect..类中实现")
    def recently_old(self, req, days):
        # return neep_study_ob
        queryset = self.get_queryset().all()
        # return self.get_queryset().filter()
        recents = []
        for item in queryset:
            b = item.recently(days=float(days))
            print("@item.recently:", b)
            if b:
                recents.append(item.id)
        # # QuerySet()
        #     # Res
        # queryset.filter(id)
        # print(recents[0])
        # return Res("tesing..")
        print("@recents:", recents)
        queryset = neep_study_ob.filter(id__in=recents)
        ser = self.serializer_class(instance=queryset, many=True)
        return Res(ser.data)


class Cet4StudyModelViewSet(ModelViewSet):
    queryset = cet4_study_ob.all()
    serializer_class = Cet4StudyModelSerializer
    filter_fields = ["user", "wid", "familiarity"]
    search_fields = filter_fields


class Cet6StudyModelViewSet(ModelViewSet):
    queryset = cet6_study_ob.all()
    serializer_class = Cet6StudyModelSerializer
    filter_fields = ["user", "wid", "familiarity"]
    search_fields = filter_fields


# class RefresherAPIView(GenericAPIView):
class RefresherModelViewSet(ModelViewSet):

    def get_queryset(self, examtype="4"):
        queryset = cet4_study_ob
        if (examtype == "cet6"):
            queryset = cet6_study_ob
        elif (examtype == "neep"):
            queryset = neep_study_ob
        # sum = queryset.all().count()
        # print(sum)
        print("@refresh:queryset:", queryset)
        return queryset

    def get_serializer_class(self, examtype='cet4'):
        # ser = None
        print("@get_serializer_class::examtype:", examtype, examtype == 'cet4')
        if (examtype == 'cet4'):
            ser = Cet4StudyModelSerializer
        # ser = Cet6StudyModelSerializer
        if (examtype == "cet6"):
            ser = Cet6StudyModelSerializer
        elif (examtype == "neep"):
            ser = NeepStudyModelSerializer
        print("@ser:", ser, "@examtype:", examtype)
        return ser

    # def get_serializer_class(self):
    # 无参的,才可以被create正确调用(同时可以接受参数来判断)

    # def get_serializer_class(self):
    #     get
    def refresh(self, req, examtype):
        print("@@refresh:刚刚捕获到请求...")
        wid = req.data.get("wid")
        user = req.data.get("user")
        # 根据参数examtype计算出需要使用的模型Manager
        queryset = self.get_queryset(examtype=examtype)
        queryset = queryset.filter(wid=wid) & queryset.filter(user=user)
        print("@@refresh:queryset:", queryset)
        # if queryset.count():
        #     instance = queryset[0]
        #     ser = self.serializer_class(instance=instance, data=req.data)#wrong!
        #     ser = self.serializer_class()(instance=instance,data=req.data)
        #     ser.is_valid()
        #     ser.save()
        #     return Res(ser.data)
        # todo 温习django的原生update(put)操作
        # return self.update(req, instance=instance)
        ser = self.get_serializer_class(examtype=examtype)
        # 最佳位置?
        self.serializer_class = ser

        if queryset.count():  # 原生方案
            instance = queryset[0]
            print("当前条目已经存在,于对应数据库,仅执行修改操作..", instance)
            # 执行一次幂等操作,使得其可以触发时间更新操作!
            # instance.wid += 0#error:外键类型wid是属于Word模型实例,而不是整型
            # 单纯的对一个未修改的对象执行一次save()操作,也可以触发modified 条件,以便于自动更新时间字段(auto_now=True)
            instance.save()
            # ser = self.serializer_class(instance=instance, data=req.data)
            tip_d = {"examtype": examtype, "msg": "modify the existed obj", "ser": str(type(ser))}
            # print(type(ser.data))
            # for item in ser.data:
            #     print(item)
            extra_d = dict(**ser(instance=instance).data, **tip_d)
            # print(type(ser.data))
            print("extra_d:", extra_d)
            return Res(extra_d, status=status.HTTP_201_CREATED)
            # return Res(ser(instance=instance).data, status=status.HTTP_201_CREATED)
        else:
            # return Res("pass..dubuging...")
            # ser = self.serializer_class(data=req.data)
            print("@self.serializer_class:", self.serializer_class)
            print("下一行执行self.create(req)")
            # 查看库文件(GenericAPI)(范围为库文件的符号查询:get_serializer)
            #     def get_serializer(self, *args, **kwargs):
            #         """
            #         Return the serializer instance that should be used for validating and
            #         deserializing input, and for serializing output.
            #         """
            #         serializer_class = self.get_serializer_class()
            #         kwargs.setdefault('context', self.get_serializer_context())
            #         return serializer_class(*args, **kwargs)
            ser = ser(data=req.data)
            # print("@req.data:", req.data)

            ser.is_valid()
            errors = ser.errors
            print("@errors:", errors)
            # return Res("pass..dubuging...")
            instance = ser.save()
            # 如果需要查看被序列化器有效接受的字段,可以再save()方法前查看data属性
            # 如果检测完毕,就将其注释掉,或者调整到下一行/或者克隆一个对象查看
            print("@ser.data:", ser.data)
            print("@instance:", instance)
            # return Res("pass..dubuging...")

            # 注意,不是所有对象都可以转化(序列化)为Json
            # 应该尽量使用基础类型,必要的时候,可以使用str()将任意类型对象转换为字符串后再塞入包装
            tip_d = {"examtype": examtype, "ser": str(type(ser))}
            # print(type(ser.data))
            # for item in ser.data:
            #     print(item)
            extra_d = dict(**ser.data, **tip_d)
            # print()
            print("@extra_d", extra_d)
            return Res(extra_d, status=status.HTTP_201_CREATED)
            # return self.create(req)

    def familiarity_change1(self, req, examtype, change="add"):
        """
        实现熟悉度的增加/减少
        :param req: 
        :type req: 
        :param examtype: 
        :type examtype: 
        :param change: add/sub
        :type change: int
        :return: 
        :rtype: 
        """
        # params=req.query_params(这是获取query_参数)
        # 获取请求体参数
        data = req.data
        user = data.get("user")
        wid = data.get("wid")
        queryset = QuerysetDispatcher.get_queryset_study(examtype=examtype)
        # study=get_object_or_404(model,user=user,wid=wid)
        # study = queryset.get(user=user, wid=wid)
        queryset = queryset.filter(user=user, wid=wid)
        # 由于前期测试数据较为随意,故而使用first()
        study = queryset.first()
        # study=queryset[0]
        if (change == "add"):
            study.familiarity = F('familiarity') + 1
        elif (change == "sub"):
            study.familiarity = F('familiarity') - 1
        study.save()
        study = queryset.filter(user=user, wid=wid).first()
        ser = QuerysetDispatcher.get_serializer_class_study(examtype=examtype)
        data = ser(instance=study).data
        return Res(data)


# class Review(ListAPIView):
#     queryset = c4ob.all()
#     serializer_class = Cet4WordsReqModelSerializer
#
#     def get(self, req, size=5):
#         # size = 5
#         if (size < 0):
#             return Res({"msg": "requirement:size>=0! "})
#         set = self.get_queryset()
#         upper = set.count()
#
#         random_words_pks = Randoms.Randoms.get_range_randoms(low=0, high=upper, contain_high=1, size=size)
#         q_in = c4ob.filter(wordorder__in=random_words_pks)
#         ser = self.serializer_class(instance=q_in, many=True)
#         return Response(ser.data)

# def list(self):
# class QuerysetDispatcher:
#     def get_queryset_study(self, examtype="4"):
#         queryset = cet4_study_ob
#         if (examtype == "cet6"):
#             queryset = cet6_study_ob
#         elif (examtype == "neep"):
#             queryset = neep_study_ob
#         # sum = queryset.all().count()
#         # print(sum)
#         print("@dispatcher:queryset_study:", queryset)
#         return queryset
#
#     def get_queryset_reqs(self, examtype="4"):
#         # 考纲表manager
#         queryset = c4ob
#         if (examtype == "cet6"):
#             queryset = c6ob
#         elif (examtype == "neep"):
#             queryset = neepob
#         # sum = queryset.all().count()
#         # print(sum)
#         print("@dispatcher:queryset_reqs:", queryset)
#         return queryset
#
#     def get_serializer_class_reqs(self, examtype="4"):
#         ser = Cet4WordsReqModelSerializer
#         if (examtype == "cet6"):
#             ser = Cet6WordsReqModelSerializer
#         elif (examtype == "neep"):
#             ser = NeepWordsReqModelSerializer
#         print("@dispatcher:", ser)
#         return ser


class RandomInspectionModelViewSet(ModelViewSet):
    get_queryset = QuerysetDispatcher.get_queryset_req
    get_serializer_class = QuerysetDispatcher.get_serializer_class_req

    def get_words_random(self, req, examtype, size):
        # size = 5
        if (size < 0):
            return Res({"msg": "requirement:size>=0! "})
        # fuck.
        # set = self.get_queryset()
        ser = self.get_serializer_class(examtype=examtype)
        queryset = self.get_queryset(examtype=examtype)
        upper = queryset.count()
        random_words_pks = Randoms.get_range_randoms(low=0, high=upper, contain_high=1, size=size)

        print("尝试调用get_queryset(my code)..")
        print("@queryset:", queryset, queryset.count())
        q_in = queryset.filter(wordorder__in=random_words_pks)
        # print()
        # str(object)比str(type(object))更加管用.
        tip_d = {"examtype": examtype, "queryset": str(queryset), "ser": str(ser)}
        ser = ser(instance=q_in, many=True)
        # print(ser.data)
        # extra_d = {**tip_d, **ser.data}
        # from collections import OrderedDict
        tip_od = OrderedDict(tip_d)
        # extra_od = [tip_od[key] = ser.data[key]
        # for key in ser.data]
        ser_data = ser.data
        # print(tip_od, data_od)
        # print("@tip_od:", type(tip_od))
        # print1(tip_od)
        # print("@ser_data:",type(ser_data))
        # print1(ser_data)
        # list of OrderedDict
        extra_od = [tip_od]
        for item in ser_data:
            extra_od.append(item)

        # data
        # ser_data
        # for key in ser_data:
        #     tip_od[key] = ser_data[key]
        # return Res("testing")
        return Res(extra_od)
        # return Response(ser.data)


class NeepStudyDetailViewSet(ReadOnlyModelViewSet):
    queryset = neep_study_ob.all()
    serializer_class = NeepStudyDetailModelSerializer
    # pass
