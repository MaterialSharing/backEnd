from collections import OrderedDict

from django.db.models import F
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from cxxulib.querysetDispatcher import QuerysetDispatcher
from cxxulib.randoms import Randoms
from cxxulib.static_values import Res, study_ob
from scoreImprover.serializer import StudyModelSerializer


class StudyModelViewSet(ModelViewSet):
    queryset = study_ob.all()
    serializer_class = StudyModelSerializer
    filter_fields = ["user", "wid", "familiarity", "examtype"]
    search_fields = filter_fields

    def refresh(self, req):
        # examtype 这里采用query_parameters
        # params = req.query_params #for post/put it is wrong,it just for get!
        params = req.data
        print(params)
        # return Res(params)
        examtype = params.get("examtype", None)
        # print(examtype)
        if not examtype:
            return Res({"msg": "examtype required!"})
        print("@@refresh:刚刚捕获到请求...by:", self.__class__.__name__)
        wid = req.data.get("wid")
        user = req.data.get("user")
        # 根据参数examtype计算出需要使用的模型Manager
        queryset = self.get_queryset()
        queryset = queryset.filter(wid=wid) & queryset.filter(user=user)
        queryset = queryset & queryset.filter(examtype=examtype)
        # queryset=queryset.first()
        print("@@refresh:queryset:", queryset)

        ser = self.get_serializer_class()
        # 最佳位置?
        self.serializer_class = ser

        if queryset.count():  # 原生方案
            instance = queryset[0]
            print("当前条目已经存在,于对应数据库,仅执行修改操作..", instance)
            instance.save()
            # ser = self.serializer_class(instance=instance, data=req.data)
            tip_d = {"msg": "modify the existed obj", "ser": str(type(ser))}
            # print(tip_d)
            # print(ser(instance=instance).data)
            extra_d = dict(**ser(instance=instance).data)
            extra_d = dict(**ser(instance=instance).data, **tip_d)
            print("extra_d:", extra_d)
            # return Res("debuging..")
            # print(type(ser.data))
            return Res(extra_d, status=status.HTTP_201_CREATED)
            # return Res(ser(instance=instance).data, status=status.HTTP_201_CREATED)
        else:
            # return Res("pass..dubuging...")
            # ser = self.serializer_class(data=req.data)
            print("@self.serializer_class:", self.serializer_class)
            print("下一行执行self.create(req)")
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

            tip_d = {"ser": str(type(ser))}
            # print(type(ser.data))
            # for item in ser.data:
            #     print(item)
            extra_d = dict(**ser.data, **tip_d)
            # print()
            print("@extra_d", extra_d)
            return Res(extra_d, status=status.HTTP_201_CREATED)
            # return self.create(req)

    def familiarity_change1(self, req, change="add"):
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
        queryset = self.get_queryset()
        # study=get_object_or_404(model,user=user,wid=wid)
        # study = queryset.get(user=user, wid=wid)
        queryset = queryset.filter(user=user, wid=wid)
        # 由于前期测试数据较为随意,故而使用first()
        study = queryset.first()
        if (not study):
            return Res({"msg": "Study not found"}, status.HTTP_404_NOT_FOUND)
        # study=queryset[0]
        if (change == "add"):
            study.familiarity = F('familiarity') + 1
        elif (change == "sub"):
            study.familiarity = F('familiarity') - 1
        study.save()
        study = queryset.filter(user=user, wid=wid).first()
        # ser = QuerysetDispatcher.get_serializer_class_study(examtype=examtype)
        ser = self.get_serializer_class()
        data = ser(instance=study).data
        return Res(data)

    def get_words_random(self, req, examtype, size):
        # size = 5
        if (size < 0):
            return Res({"msg": "requirement:size>=0! "})
        # fuck.
        # set = self.get_queryset()
        ser = self.get_serializer_class()
        # queryset = self.get_queryset(examtype=examtype)
        queryset = self.queryset
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
