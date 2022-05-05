# from django.shortcuts import render
import json

import django.http
from django.http import JsonResponse
from django.http import HttpResponse
from django.views import View
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin

from user.models import User
from rest_framework import serializers
from user.serializer import UserSerializer

# from django.urls
# Create your views here.
uob = User.objects


# 使用DRF ViewSet视图集的方式来开发
class UserApiViewSet(ModelViewSet):
    # query_set = uob.all()
    # 要求用queryset这个视图类的字段名称)
    queryset = uob.all()
    serializer_class = UserSerializer
    requeryset = uob.all()
    serializer_class = UserSerializer

    def get(self, request):
        return self.list(request)


# 使用Django原生的方式开发Restful api
class UserApiView(View):
    def get(self, reqeust, pk=-1):
        print("@pk", pk)
        # 查询所有用户
        uob = User.objects
        query_set = uob.all()
        if (pk == -1):
            pass
        else:
            # query_set = uob.get(pk=pk)
            query_set = uob.filter(pk=pk)
        user_list = []
        for user in query_set:
            user_list.append(
                {
                    "uid": user.uid,
                    "name": user.name,
                    "singin": user.signin,

                }
            )
        print("get it!")
        return django.http.JsonResponse(user_list, safe=False)

    def post(self, request):
        print("get post req")
        # get byte code from the request body
        json_bytes = request.body
        # get str by decode the byte code.
        json_str = json_bytes.decode()
        # get dict object
        user_dict = json.loads(json_str)
        print(user_dict)
        # get user object which will be posted to the table
        # it will show what was posted (insert to database)
        # User->UserInfo
        user = User.objects.create(
            #     several filed:values pairs
            name=user_dict.get("name"),
            signupdate=user_dict.get("signupdate")
        )
        # 返回插入操作的结果(由于参数是字典,而不是数组,不用参数save=False)
        return JsonResponse({
            "uid": user.uid,
            "name": user.name,
            "signupdate ": user.signupdate
        })

    def put(self, request, pk):
        print("@get put request!")
        uob = User.objects
        try:
            user = uob.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse("the user does not exist yet!")
        json_bytes = request.body
        json_str = json_bytes.decode()
        user_dict = json.loads(json_str)
        print(user_dict.get("name"))
        # update the table
        user.name = user_dict.get("name")
        user.id = user_dict.get("uid")
        # confirm the operation to execute
        user.save()

        return JsonResponse(
            {
                "name": user.name,
                "signupdate": user.signupdate
            }
        )

    def delete(self, request, pk):
        print("@delete request captured!")
        uob = User.objects
        try:
            user = uob.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse("the user does not exist yet!")
        # update the table
        print(user)
        user.delete()
        # deleted successful,then just return HttpResponse status code (rather than json)
        return HttpResponse(status=204)


# 初始的版本
class ListViewRaw(ListModelMixin, GenericAPIView):
    # 定义queryset,该属性字段将有DRF框架内来(使用)
    # print("try to invoke authentication ")
    queryset = uob.all()
    # 定义serializer_class,指定对应的模型类序列化器,同样有DRF来使用.
    serializer_class = UserSerializer

    def get(self, request):
        return self.list(request)


class DIYPagination(PageNumberPagination):
    #     自定义分页器配置
    page_query_param = 'pager'  # 默认是page
    page_size = 4  # 每一页可以显示的条数
    max_page_size = 50  # 前端最多可以请求到第50页


class ListView(ListAPIView):
    # 简化继承后的版本(ListAPIView
    print("@@try to invoke authentication ")
    # permission_classes = [IsAuthenticated]
    queryset = uob.all()
    serializer_class = UserSerializer
    filter_fields = ('name', 'signupdate')
    filter_backends = [OrderingFilter]
    # http://127.0.0.1:8000/user/?ordering=uid
    # http://127.0.0.1:8000/user/?ordering=-signin
    ordering_fileds = ("uid", "name", "signupdate", "signin")
    # query过滤式子:
    # /user/?name=cxxu_testSer
    # http://127.0.0.1:8000/user/?signupdate=1970-01-01
    # 分页pagination
    # 再settings中配置分页后,可以结合排序一起使用
    # http://127.0.0.1:8000/user/?page=2&ordering=uid
    # 关闭全局分页的配置:
    # pagination_class = None
    # 自定义分页器规则类
    pagination_class = DIYPagination

    ###
    # def get()等就不用再写了.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.\n content provided by poll/view.py")


def userAdd(request, name):
    print("try to add demo user..")
    # 实例化一个新对象,用以增加和修改表的记录
    ob = User()
    # print(ob.objects.all())
    print(ob)
    print(type(ob))
    ob.name = name
    ob.examDate = '2021-10-11'
    ob.examType = '6'
    ob.signIn = 33
    # 使用save执行
    ob.save()
    return HttpResponse(f"{ob.name} added!")


def userDelete(request, name):
    print("try to delete user%s" % (name))
    # t:table
    modUser = User.objects
    user = modUser.all()


def userCheck(request, name):
    print("try user check..")
    ob = User.objects
    try:

        users = ob.all()
        for user in users:
            print(user)
            print()
        # ob.get(name='cxxu')
        res = ob.get(name=name)
        print(f'@res={res}')
        return HttpResponse(res)
    except:
        return HttpResponse("no specified user exist yet !")
