import json

import django.http
from deprecated.classic import deprecated
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet, ReadOnlyModelViewSet

from cxxulib.static_values import uob, Res
from user.models import User
from user.serializer import UserSerializer, UserModelSerializer
from word.paginations import DIYPagination


@deprecated
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.\n content provided by poll/view.py")


@deprecated
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


@deprecated
def userDelete(request, name):
    print("try to delete user%s" % (name))
    # t:table
    modUser = User.objects
    user = modUser.all()


@deprecated
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


# 使用Django原生的方式开发Restful api
@deprecated
class UserView(View):
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
        # return HttpResponse(status=204)
        return JsonResponse(data={}, status=204)


@deprecated()
class UserSer0View(View):
    """
    def post(self,request):
    反序列化-采用字段选项来验证数据"
    #1．接收客户端提交的数据
    #1.1实例化序列化器，获取序列化对象
    # 1.2调用序列化器进行数据验证
    # 1.3 获取验证以后的结果
    # 2．操作数据库
    返回结果
    """

    def get_get(self, request):
        """序列化:从后台查询数据经过处理(序列化处理),在返回给客户端"""
        # 从数据库中查询到数据集(User对象)
        users = uob.all()
        # 基于查询到的数据集,构造出序列化器对象,此时的序列号对象中包含了查询到的数据,我们可以方便的调用data方法,得到类似字典的数据
        # 字段情况由 我们之前定义的序列化器来决定(有了序列化器,我们就不用在通过手动的将查询到得到数据进行拆解并和构造字典
        user_ser = UserSerializer(instance=users, many=True)
        # 调用经过装饰器处理过的属性方法
        data = user_ser.data
        # 通过JsonResponse 将得到data转化为需要的jsonL类型数,并返回
        '''反序列化:与序列相反的方向操作数据
        - 数据验证
        使用序列化器进行反序列化时，需要对数据进行验证后，才能获取验证成功的数据或保存成模型类对象。
        在获取反序列化的数据前，必须调用is_valid()方法进行验证，验证成功返回True，否则返回False。
        验证失败，可以通过序列化器对象的errors属性获取错误信息，返回字典，包含了字段和字段的错误。
            如果是非字段错误，可以通过修改REST framework配置中的NON_FIELD_ERRORS_KEY来控制错误字典中的键名。
        验证成功，可以通过序列化器对象的validated _data属性获取数据。
        在定义序列化器时，指明每个字段的序列化类型和选项参数，本身就是一种验证行为。
        选项参数:参数名称
            作用
            max_length            最大长度
            min_lenght            最小长度
            allow_blank            是否允许为空
            trim_whitespace            是否截断空白字符
            max_value            最小值
            min_value            最大值

        通用参数:参数名称
        read_only       表明该字段仅用于序列化输出，默认False
        write_only      表明该字段仅用于反序列化输入，默认False
        required        表明该字段在反序列化时必须输入，默认True
        default     反序列化时使用的默认值
        allow_null      表明该字段是否允许传入None，默认False
        validators      该字段使用的验证器
        error_messages      包含错误编号与错误信息的字典
        label           用于HTML展示API页面时，显示的字段名称
        help_text       用于HTML展示API页面时，显示的字段帮助提示信息

        #字段= serializers .字段类型(选项=选项值,)
        id = serializers.IntegerField(read only=True)# read_only=True，在客户端提交数据[反序列化阶段不会要求id字段]name = serializers.charField(required=True) # required=True ，反序列化阶段必填
        sex = serializers.BooleanField(default=True) # default=True，反序列化阶段，客户端没有提交，则默认为Trueage = serializers.IntegerField(max value=100，min value=0).# age在反序列化必须是0 <= age <= 100
        description = serializers.CharField(allow null=Trtle，allow blank=True)# 允许客户端不填写内容(None)
        或者值为“"
        '''
        return JsonResponse(data=data, status=200, safe=False, json_dumps_params={"ensure_ascii": False})

    # 将默认get路由模拟成post(添加数据)
    def get_create(self, request):
        """
        :param request:
        :type request:
        :return:
        :rtype:
        """
        # 内建一个用户测试的数据(data字典),来测试validate功能的基本可用性
        data = {
            "name": "create_ser_pyt",
            "signin": 778,
        }
        # 这里先用模拟post请求是将验证表单提交的数据是否符合规范
        user_ser = UserSerializer(data=data)
        # 调用序列化器对象的验证方法进行验证.
        # 通过参数raise_exception=True控制是否抛出异常(如果抛出,后续代码将不在执行)
        user_ser.is_valid(raise_exception=True)
        # 获取验证后的结果
        data = user_ser.validated_data
        # 后台查看校验结果
        print(data)
        # 将验证通过的对象解包,作为参数传递给create方法,以添加一条记录
        # 操作数据库,接受操作返回的模型对象
        # user = uob.create(**data)
        # 检查添加后的结果(再次基于返回的模型对象(记录对象)实例化出来的序列化器,并借助该对象的data方法,得到类字典的数据
        # user_ser = UserSerializer(instance=user)
        # 会根据实例化serializer时,是否传入instance 属性来判断是否子弟哦那个调用update方法,如果没有传入,则自动调用create()
        user_ser.save()
        user_data = user_ser.data
        return JsonResponse(user_data, status=201)
        # ret=user_ser.is_valid()
        '''
        # def __init__(self, instance=None, data=empty, **kwargs):

       if self.instance is not None:
            # 如果构造序列化器时,有传入实例(会被认为时要修改该实例(instance),所以这里会调用序列化器中的(我们自己实现的名为update的方法来更新记录
            # 体现在view中就是使用serializer.save来自动处理(包括后面的create(),create的时候,没有传入instance实例,就会调用序列化器对象中(同样是自己实现的函数,且名为create
            # 方法.
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            self.instance = self.create(validated_data)
            assert self.instance is not None, (
                '`create()` did not return an object instance.'
            )

            '''

    #     将以上函数作为对象,赋值给get
    def get(self, request):
        # return Json/httpResonse boject
        s = self
        # get = s.get_create
        return s.get_create(request)

    def get_put(self, request):
        """
        将默认路由模拟为put(修改一条记录)
        :param request:
        :type request:
        :return:
        :rtype:
        """
        pk = 7
        try:
            user = uob.get(pk=pk)
        except User.DoesNotExist:
            return JsonResponse({"errors": "the user does not exist!"})
        # 模拟记录需要修改的字段
        data_d = {
            "name": "pyta",
            "signin": 178,
        }
        # 实例化序列化器
        user_ser = UserSerializer(instance=user, data=data_d)  # 可以传入partial=True
        #  先利用序列化器检查(is_valid()调用)一下客户端传入的数据(或者我们模拟出来的数据是否符合要求)
        user_ser.is_valid(raise_exception=True)
        # 数据通过检查规范,执行入库操作

        user_ser.save()  # 这里传递的参数给save()可以免除验证
        return JsonResponse(user_ser.data, status=201)


@deprecated()
class UserSerView(View):

    def get_get(self, request):
        """序列化:从后台查询数据经过处理(序列化处理),在返回给客户端"""
        # 从数据库中查询到数据集(User对象)
        users = uob.all()
        # 基于查询到的数据集,构造出序列化器对象,此时的序列号对象中包含了查询到的数据,我们可以方便的调用data方法,得到类似字典的数据
        # 字段情况由 我们之前定义的序列化器来决定(有了序列化器,我们就不用在通过手动的将查询到得到数据进行拆解并和构造字典
        user_ser = UserModelSerializer(instance=users, many=True)

        # 调用经过装饰器处理过的属性方法
        data = user_ser.data
        # 通过JsonResponse 将得到data转化为需要的jsonL类型数,并返回

        return JsonResponse(data=data, status=200, safe=False, json_dumps_params={"ensure_ascii": False})

    # 将默认get路由模拟成post(添加数据)
    def get_create(self, request):

        # 内建一个用户测试的数据(data字典),来测试validate功能的基本可用性
        data = {
            "name": "create_ser_M_pyt",
            "signin": 8,
            # "nickname":"extra filed by serializerDef"
        }
        # 这里先用模拟post请求是将验证表单提交的数据是否符合规范
        user_ser = UserModelSerializer(data=data)
        # 调用序列化器对象的验证方法进行验证.
        # 通过参数raise_exception=True控制是否抛出异常(如果抛出,后续代码将不在执行)
        user_ser.is_valid(raise_exception=True)
        # 获取验证后的结果
        data = user_ser.validated_data
        # 后台查看校验结果
        print(data)
        # 将验证通过的对象解包,作为参数传递给create方法,以添加一条记录
        # 操作数据库,接受操作返回的模型对象
        # user = uob.create(**data)
        # 检查添加后的结果(再次基于返回的模型对象(记录对象)实例化出来的序列化器,并借助该对象的data方法,得到类字典的数据
        # user_ser = UserSerializer(instance=user)
        user_ser.save()  # 会根据实例化serializer时,是否传入instance 属性来判断是否子弟哦那个调用update方法,如果没有传入,则自动调用create()
        user_data = user_ser.data
        return JsonResponse(user_data, status=201)
        # ret=user_ser.is_valid()

    def get_put(self, request):
        """
        将默认路由模拟为put(修改一条记录)
        :param request:
        :type request:
        :return:
        :rtype:
        """
        pk = 7
        try:
            user = uob.get(pk=pk)
        except User.DoesNotExist:
            return JsonResponse({"errors": "the user does not exist!"})
        # 模拟记录需要修改的字段
        data_d = {
            "name": "pyta",
            "signin": 178,
        }
        # 实例化序列化器
        user_ser = UserModelSerializer(instance=user, data=data_d)  # 可以传入partial=True
        #  先利用序列化器检查(is_valid()调用)一下客户端传入的数据(或者我们模拟出来的数据是否符合要求)
        user_ser.is_valid(raise_exception=True)
        # 数据通过检查规范,执行入库操作

        user_ser.save()  # 这里传递的参数给save()可以免除验证
        return JsonResponse(user_ser.data, status=201)
        #     将以上函数作为对象,赋值给get

    def get(self, request):
        # return Json/httpResonse boject
        s = self
        # get = s.get_create # wrong,without request parameter!
        # return s.get_get(request)
        return s.get_create(request)
        # return s.get_put(request)


"""
APIView是REST framework提供的所有视图类的基类，继承自Django的 view父类。
APIView与view的不同之处在于:
·传入到视图方法中的是REST framework的Request对象，而不是Django的HttpRequeset对象;
·视图方法可以返回REST framework的 Response对象，视图会为响应数据设置(renderer）符合前端期望要求的格式;
·任何APIException异常都会被捕获到，并且处理成合适格式的响应信息返回给客户端;django的View中所有异常全部以HTML格式显示
drf的APIVlew或者APIView的子类会自动根据客户端的Accept进行错误信息的格式转换。
·重新声明了一个新的as_view方法并在dispatch()进行路由分发前，会对请求的客户端进行身份认证、权限检查、流量控制。
APIView除了继承了View原有的属性方法意外，还新增了类属性:
authentication_classes列表或元组，身份认证类
- permissoin_classes列表或元组，权限检查类**throttle_classes**列表或元祖，流量控制类
"""


# 编写基于drf提供的APIView的子类视图
# 尝试基于ApiView实现常用的5中类型接口,可以将这5个接口划分为2部分(拆分给两个视图类来负责)
# 根据路由url是否带有参数:(将接口分散到多个视图类中)
# 一个类负责处理带有参数(pk)(查询/修改/删除)某个id)
# 另一个负责不需要带参数的(譬如查询所有/添加一条记录(id自增)

# 此时的简化还是有限的,无法更加通用(可以通过genericAPIView进一步优化

# APIView是REST framework提供的所有视图的基类，继承自Django的View父类。
#
# drf的APIView与djangoView的不同之处在于：
#
# 传入到视图方法中的是REST framework的Request对象，而不是Django的HttpRequeset对象；
# 视图方法可以返回REST framework的Response对象，视图会为响应数据设置（render）符合前端要求的格式；
# 任何APIException异常都会被捕获到，并且处理成合适的响应信息；
# 重写了as_view()，在进行dispatch()路由分发前，会对http请求进行身份认证、权限检查、访问流量控制。
# 支持定义的类属性
#
# authentication_classes 列表或元组，身份认证类
# permissoin_classes 列表或元组，权限检查类
# throttle_classes 列表或元祖，流量控制类
# 在APIView中仍以常规的类视图定义方法来实现get() 、post() 或者其他请求方式的方法。
@deprecated()
class UserAPIView(APIView):
    def get(self, req):
        # print(f"drf.request={request}")
        print(f"django.reqeust={req._request}")  # WSGIHttpRequest
        print(f"@@!Meta={req._request.META.get('Accept')}")
        # print(f"reqeust.query_parames={req.query_params}")
        # return Response({"msg":"ookk"})
        # 有些参数会引起apifox提示header token error!
        # headers={"@@test":"line by cxxu Response"}
        users = uob.all()
        users_ser = UserModelSerializer(instance=users, many=True)
        return Res(users_ser.data)
        return Response({"msg": "ok(drfResponse)"}, status=status.HTTP_200_OK)

    def post(self, req):
        # user_apiView/?test_param=abc
        # print(f"req.data={req.data}")
        # print(req.data.get("name"))
        # print(f"req.query_params={req.query_params}")
        print(f"django.reqeust={req._request}")  # WSGIHttpRequest
        print(f"@@@Meta={req._request.META.get('Accept')}")

        user_ser = UserModelSerializer(data=req.data)
        # 依然是实例化序列化器并验证数据
        user_ser.is_valid(raise_exception=True)
        user_ser.save()
        # 返回数据+状态码
        return Response(user_ser.data, status=status.HTTP_201_CREATED)
        # 我们也可以实验一下drf提供的返回错误信息(json)的功能(而不是简单的抛出错误终止运行.)
        """
        {
            "signin": [
                "sign should meet :sign<100000"
            ]
        }
        {
        "signin": [
        "sign should meet :sign>=0"
        ]
        }
        """
        return Response({"msg": "ok(drf_post)"})


@deprecated()
class UserInfoAPIView(APIView):
    def get(self, req, pk):
        try:
            user = uob.get(pk=pk)
        except User.DoesNotExist:
            return Res(status=status.HTTP_404_NOT_FOUND)
        user_ser = UserModelSerializer(instance=user)
        # print(req)
        # print(f"@req.data={req.data}")
        return Res(user_ser.data)

    def put(self, req, pk):
        try:
            # user = uob.get(pk)#wrong!,use keyword parameter please!
            user = uob.get(pk=pk)
            print(user)
        except User.DoesNotExist:
            return Res(status=status.HTTP_404_NOT_FOUND)
        # 修改比添加和删除需要多出传入目标数据(被修改的对象instance需要被修改成什么样(或者说哪些字段data需要修改)
        # req.data比django原生req.body.data方便
        print(req)
        print(f"😂😂😂😂@req.data={req.data}")
        user_ser = UserModelSerializer(instance=user, data=req.data)
        user_ser.is_valid(raise_exception=True)
        user_ser.save()
        return Res(user_ser.data, status=status.HTTP_201_CREATED)
        # return Res({"msg": "tesing..."})

    def delete(self, req, pk):
        try:
            # user = uob.get(pk)#wrong!,use keyword parameter please!
            user = uob.get(pk=pk)
            user.delete()
            # print(user)
        except User.DoesNotExist:
            return Res(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


# 使用genericAPIView处理通用代码
# 再genericAPIView中,通过浏览器访问的界面中进一步增强了具体性,其中特别是根据数据模型,创建了一个较为方便的表单视图(在APIView中仅有一个总体的框框)
# 同时,错误信息进一步改善,可以将错误返回为一个json
# 通用代码进一步抽象成基类,可以被子类继承复用
@deprecated()
class UserGenericAPIView(GenericAPIView):
    """
    这些属性(代码不可共用(直接涉及到具体的模型),将它们提前到类属性中),而不是作为成员方法的内部变量.
    """
    # 固定属性queryset(必填)
    queryset = uob.all()
    # 默认序列化器指定(选填)
    serializer_class = UserModelSerializer

    def get(self, req):
        # 我们采用框架规范建议的方式(使用方法来引用类型属性)
        queryset = self.get_queryset()  # 主要效果就是self.queryset(当然,通过函数来引用类变量,我们可以再对类变量做一些加工(判断)等处理
        ser = self.get_serializer(instance=queryset, many=True)  # 这一句也类似self.serializer_class
        return Res(ser.data)

    def post(self, req):
        ser = self.get_serializer(data=req.data)
        # 数据的修改(put->create)/增加(post->create)需要is_valid();然后再save(),比较通用的操作
        ser.is_valid(raise_exception=True)
        ser.save()
        return Res(ser.data, status=status.HTTP_201_CREATED)


@deprecated()
class UserInfoGenericAPIView(GenericAPIView):
    queryset = uob.all()
    # 默认序列化器
    serializer_class = UserModelSerializer

    # 重写序列化器指定方法
    # def get_serializer_class(self):
    #         """重写获取序列化器类的方法"""
    #         if self.request.method == "GET":
    #             return StudentModel2Serializer
    #         else:
    #             return StudentModelSerializer
    def get(self, req, pk):
        ins = self.get_object()
        # keyword name must be `instance`(by source code of DRF
        ser = self.get_serializer(instance=ins)
        return Res(ser.data)

    def put(self, req, pk):
        ins = self.get_object()
        ser = self.get_serializer(instance=ins, data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Res(ser.data, status=status.HTTP_201_CREATED)

    def delete(self, req, pk):
        ins = self.get_object()
        ins.delete()
        return Res(status=status.HTTP_204_NO_CONTENT)


# 使用DRF ViewSet视图集的方式来开发(多个个迭代)
# 原生+drf_serializer版本
'''1.使用序列化器的时候一定要注意，序列化器声明了以后，不会自动执行，需要我们在视图中进行调用才可以。
2.序列化器无法直接接收数据，需要我们在视图中实例化序列化器对象时把使用的数据传递过来。
3.序列化器的字段声明类似于我们前面使用过的模型。
4.开发restful api时，序列化器会帮我们把模型对象转换成字典
5. drf提供的视图会帮我们把字典转换成json,或者把客户端发送过来的数据转换字典.
'''

# 版本(多继承版本): ListModelMixin,GenericApiView
# 基于GenericApiView,我们再继承一个类,该类提供了通用的某个CRED的操作.
# 作用:
# 提供了几种后端视图(对数据资源进行增删改查)处理流程的实现，如果需要编写的视图属于这五种，则视图可以通过继承相应的扩展类来复用代码，减少自己编写的代码量。
# 这五个扩展类需要搭配GenericAPIView通用视图基类，因为五个扩展类的实现需要调用GenericAPIView提供的序列化器与数据库查询的方法。

# 使用drf内置的模型扩展类[混入类]结合GenericAPIView实现通用视图方法的简写操作
# from rest_framework.mixins import ListModelMixin获取多条数据，返回响应结果  # list _
# from rest_framework.mixins import CreateModelMixin添加一条数据，返回响应结果  # create
# from rest_framework.mixins import RetrieveModelMixin 获取一条数据，返回响应结果  # retrie
# from rest_framework.mixins import UpdateModelMixin 更新一条数据，返回响应结果  # update
# from rest_framework.mixins import DestroyModelMixin 删除一条数据，返回响应结果  # destro

"""更进一步:

上面的接口代码还可以继续更加的精简，drf在使用GenericAPIView和Mixins进行组合以后，还提供了`视图子类`。
`视图子类`是`通用视图类和模型扩展类的子类`，提供了各种的`视图方法调用mixins操作`
ListAPIView = GenericAPIView + ListModelMixin 获取多条数据的视图方法
CreateAPIView = GenericAPIView + CreateModelMixin 添加一条数据的视图方法
RetrieveAPIView = GenericAPIView + RetrieveModelMixin 获取一条数据的视图方法
UpdateAPIView = GenericAPIView + UpdateModelMixin 更新一条数据的视图方法
DestroyAPIView = GenericAPIView + DestroyModelMixin 删除一条数据的视图方法组合视图子类
组合视图的子类:
ListCreateAPIView = ListAPIView + CreateAPIView
DestroyAPIView = RetrieveAPIView + DestroyAPIView
RetrieveUpdateAPIView = RetrieveAPIView + UpdateAPIViewRetrieve
RetrieveUpdateDestroyAPIView = RetrieveAPIView + UpdateAPIView + DestroyAPIView

"""
# 使用混入类
"""Mixin提供的api界面进一步完善,可以自动完成分页显示等效果"""


@deprecated()
class UserGenericMixin(GenericAPIView, ListModelMixin, CreateModelMixin):
    # 定义queryset,该属性字段将由DRF框架内来(使用)
    # print("try to invoke authentication ")
    queryset = uob.all()
    # 定义serializer_class,指定对应的模型类序列化器,同样DRF来使用.
    serializer_class = UserModelSerializer

    def get(self, req):
        return self.list(req)

    def post(self, req):
        return self.create(req)


@deprecated()
class UserInfoGenericMixin(GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = uob.all()
    serializer_class = UserModelSerializer

    def get(self, req, pk):
        return self.retrieve(req, pk=pk)

    def put(self, req, pk):
        return self.update(req, pk=pk)

    def delete(self, req, pk):
        return self.destroy(req, pk=pk)


# class ListCreateAPIView(mixins.ListModelMixin,
#                         mixins.CreateModelMixin,
#                         GenericAPIView):

# 使用视图子类,根据接口功能来继承视图类
# class UserListCreateAPIView(ListAPIView,CreateAPIView):
@deprecated()
class UserListCreateAPIView(ListCreateAPIView):
    queryset = uob.all()
    serializer_class = UserModelSerializer

    # @override list method (derived from ListAPIView)
    # def list(self):
    #     pass


# 简化继承后的版本(ListAPIView)
# class ListAPIView(mixins.ListModelMixin,
#                   GenericAPIView
@deprecated
class ListView(ListAPIView):
    # print("@@try to invoke authentication ")
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


# class UserRetrieveUpdateAPIView(RetrieveAPIView,UpdateAPIView):
@deprecated
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = uob.all()
    serializer_class = UserModelSerializer


@deprecated
class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = uob.all()
    serializer_class = UserModelSerializer



"""上面的接口在实现过程中，也存在了代码重复的情况，我们如果合并成一个接口类，则需要考虑2个问题;1．路由的合并问题
2. get方法重复问题
drf提供了视图集可以解决上面的问题ViewSet-->基本视图集
解决APIView中的代码重复问题
GenericViewSet -->通用视图集
解决APIView中的代码重复问题，同时让代码更加"""


@deprecated
class UserViewSet(ViewSet):
    """此时基于APIView的整合"""

    def get_user_info(self, req, pk):
        # 拷贝UserAPIView的事项.
        try:
            user = uob.get(pk=pk)
        except User.DoesNotExist:
            return Res(status=status.HTTP_404_NOT_FOUND)
        user_ser = UserModelSerializer(instance=user)
        print(req)
        print(f"@req.data={req.data}")
        return Res(user_ser.data)

    def get_all(self, req):
        # 我们采用框架规范建议的方式(使用方法来引用类型属性)
        queryset = self.get_queryset()  # 主要效果就是self.queryset(当然,通过函数来引用类变量,我们可以再对类变量做一些加工(判断)等处理
        ser = self.get_serializer(instance=queryset, many=True)  # 这一句也类似self.serializer_class
        return Res(ser.data)

    def post(self, req):
        ser = self.get_serializer(data=req.data)
        # 数据的修改(put->create)/增加(post->create)需要is_valid();然后再save(),比较通用的操作
        ser.is_valid(raise_exception=True)
        ser.save()
        return Res(ser.data, status=status.HTTP_201_CREATED)

    def update(self, req, pk):
        try:
            # user = uob.get(pk)#wrong!,use keyword parameter please!
            user = uob.get(pk=pk)
            print(user)
        except User.DoesNotExist:
            return Res(status=status.HTTP_404_NOT_FOUND)
        # 修改比添加和删除需要多出传入目标数据(被修改的对象instance需要被修改成什么样(或者说哪些字段data需要修改)
        # req.data比django原生req.body.data方便
        print(req)
        print(f"😂😂😂😂@req.data={req.data}")
        user_ser = UserModelSerializer(instance=user, data=req.data)
        user_ser.is_valid(raise_exception=True)
        user_ser.save()
        return Res(user_ser.data, status=status.HTTP_201_CREATED)
        # return Res({"msg": "tesing..."})

    def delete(self, req, pk):
        ins = self.get_object()
        ins.delete()
        return Res(status=status.HTTP_204_NO_CONTENT)


"""
我们可以继续让一些合并的视图集父类让视图继承即可。
ReadOnlyModelViewSet:获取多条数据+获取一条数据:
ReadOnlyModelViewSet = mixins.RetrieveModelMixin + mixins .ListModelMixin，+ GenericViewSet

ModelViewSet
实现了5个API接口

"""


@deprecated
class UserGenericViewSet(GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = uob.all()
    serializer_class = UserModelSerializer


# ReadOnlyModelViewSet+Mixin
@deprecated()
class UserReadOnlyMixin(ReadOnlyModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = uob.all()
    serializer_class = UserModelSerializer
