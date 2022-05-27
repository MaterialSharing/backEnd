# from django.shortcuts import render
import hashlib
import json
import random
from datetime import timedelta

import django.http
from deprecated.classic import deprecated
from django.contrib.auth.hashers import make_password
from django.db.models import F
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet, ReadOnlyModelViewSet

from cxxulib.querysetDispatcher import QuerysetDispatcher
from cxxulib.static_values import uob, Res
from scoreImprover.serializer import NeepStudyModelSerializer
from scoreImprover.views import neep_study_ob
from user.models import User, WordStar, WordSearchHistory
from user.serializer import UserSerializer, UserModelSerializer, WordStarModelSerializer, WSHModelSerializer
from word.paginations import DIYPagination

uob = User.objects
Res = Response



# ModelViewSet:将继承关系进一步简写.
"""
mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet
"""
"""
视图集中附加action的声明

在视图集中，如果想要让Router自动帮助我们为自定义的动作生成路由信息，需要使用rest_framework.decorators.action装饰器。
以action装饰器装饰的方法名会作为`action动作名`，与list、retrieve等同。

action装饰器可以接收两个参数:
- methods:声明该action对应的请求方式，列表参数- detail:声明该action的路径是否与`单一资源对应`路由前缀/<pk>/action方法名/
.True表示路径格式是xxx/<pk>/action方法名/- False表示路径格式是xxx/action方法名/- url_path:声明该action的路由尾缀。

"""

# class UserApiViewSet(ModelViewSet):
#     # 该视图-模型类继承了ModelViewSet
#     # 至少要两个字段:
#     # 一个是queryset字段(保存从数据库中查到的数据(集); 要求用queryset这个视图类的字段名称)
#     # 一个是serializer_class;该字段指定视图集要引用的序列化器
#     # 两个字段的值都体现了关联的模型(uob=User.object;UserSerializer.Meta.model->User)
#     # (序列化器中则指定了模型类,方便
#     # 序列化出具有对应键值对的需要的字典)
#     queryset = uob.all()
#     serializer_class = UserSerializer
#
#     def get(self, request):
#         return self.list(request)



wsob = WordStar.objects

class WordStarModelViewSet(ModelViewSet):
    queryset = wsob.all()
    serializer_class = WordStarModelSerializer
    filter_fields = ["spelling", "user"]

    def star_word(self, req):
        """收藏一个单词"""
        # 调用CreateModelMixin提供的create()方法,帮助我们自动完成validate等操作
        # rest_framework.mixins.CreateModelMixin def create(self,
        #            request: {data},
        #            *args: Any,
        #            **kwargs: Any) -> Response
        # 该调用直接返回一个Response对象,我们无需再手动使用Response()方法进行打包封装
        # print("@req:", req.data)
        # return self.create(req)
        # 检查序列化器行为
        # data = {"user": 22, "spelling": "apply"}
        # serializer = self.get_serializer(data=req.data)

        return self.create(req)
        # return Res({"msg": "testing.. "})


# wshob = WordSearchHistory.objects

