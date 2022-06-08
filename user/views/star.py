# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.models import User, WordStar
from user.serializer import WordStarModelSerializer

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
class WordStarLoggedModelViewSet(ModelViewSet):
    queryset = wsob.all()
    serializer_class = WordStarModelSerializer
    filter_fields = ["spelling", "user"]

    def list(self, req, *args, **kwargs):
        user_d = req.session.get("cxxu")
        uid = user_d["uid"]
        queryset = wsob.filter(user=uid)
        # ser = self.get_serializer_class()(queryset, many=True)
        # return Res(ser.data)

        # queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, req, **kwargs):
        """收藏一个单词
        :param **kwargs:
        这里重写了create方法,使得通过registoer注册的路由能够将posti请求引导到这里来
        注意,这里已经不是DRF自带的默认行为,默认行为不要求登录,但是需要将再请求体中指明
        而重写的以下逻辑不需要前端手动的将用户id写入请求体,但是却要求用户登录,而且这里采用的是session机制来获取用户信息信息
        """
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
        user_d = req.session.get("cxxu")
        uid = user_d["uid"]
        req.data["user"] = uid
        print("@req.data:", req.data)
        print("@uid", uid)
        # wsob.create(**req.data)
        ser = WordStarModelSerializer(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Res(ser.data, status=status.HTTP_201_CREATED)
        # return self.create(req)
        # return Res({"msg": "testing.. "})

    def destroy(self, req, *args):
        user_d = req.session.get("cxxu")
        uid = user_d["uid"]
        req.data["user"] = uid
        data = req.data
        queryset = self.get_queryset().filter(user=uid)
        queryset = queryset.filter(spelling=data["spelling"])
        # queryset = queryset.filter(spelling=data["spelling"])
        print("@req.data:", req.data)
        print("@queryset:", queryset)
        res = queryset.delete()
        # 注意,该操作将删除整个匹配的结果记录集合
        print("@res:", res)

        return Res({"msg": "delete success"}, status=status.HTTP_204_NO_CONTENT)

# wshob = WordSearchHistory.objects
