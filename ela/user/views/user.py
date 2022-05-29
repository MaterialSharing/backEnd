# from user.views import uob, Res
# from user.models import User
# uob=User.objects
import hashlib
import random
from datetime import timedelta

from deprecated.classic import deprecated
from django.contrib.auth.hashers import make_password
from django.db.models import F
from django.utils import timezone
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cxxulib.querysetDispatcher import QuerysetDispatcher
from cxxulib.static_values import uob, Res
from scoreImprover.serializer import NeepStudyModelSerializer
from scoreImprover.views import neep_study_ob
from user.models import User
from user.serializer import UserModelSerializer, UserRegisterModelSerializer


class UserModelViewSet(ModelViewSet):
    """
    用户信息模型(这里写的文档将会反映到接口文档中去(coreapi)
    create:创建一个新用户(注册)
    read:获取用户信息
    """
    # 这两行根据被操作的数据模型的不同而不同uob=User.object
    queryset = uob.all()
    serializer_class = UserModelSerializer
    # 过滤/分页
    filter_fields = ('name', 'signupdate', 'signin')
    # filter_backends = [OrderingFilter]
    # http://127.0.0.1:8000/user/?ordering=uid
    # http://127.0.0.1:8000/user/?ordering=-signin
    #     局部验证
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # pagination_class = DIYPagination
    # 如何修改get?
    # def get(self, req):
    #     # print(req.user)
    #     if req.user.id:
    #         print("authenticate success!")
    #     else :
    #         print("authenticate failed!")
    #     return Res({"msg":"done"})
    """method not allow 问题
    通常是发生在http action(动作名不匹配的情况下)
    譬如,某个方法是被定义为只允许put操作,但是您的请求是get或者post操作,那么就会触发method not allowed!"""

    # HTTP 405 Method Not Allowed
    # Allow: PUT, OPTIONS
    # Content-Type: application/json
    # Vary: Accept
    #
    # {
    #     "detail": "Method \"GET\" not allowed."
    # }
    # 在urls.py中,本函数被指定为put操作
    # @property

    def recently_unitable(self, req, pk):
        # unit = 'days', value = 8, examtype = 'neep'
        # print("@@hhh!")
        """正在开发query参数"""
        # 指定考试类型
        params_d = req.query_params
        print("@params:", params_d)
        examtype = params_d.get("examtype", "neep")
        # timedelta的指定元素
        # 指定默认值
        unit = "days"
        value = 8
        examtype = "neep"

        # 一般情况下(用户要么传入非空值/要么不传入对应参数),那么只需要像下面这样写
        # unit = params_d.get("unit", "days")
        # value = params_d.get("value", 8)
        # 为了增强robust,做了如下讨论
        # 下面讨论根据用户传入的各种情况对默认更新或者不更新
        # 方案1:
        # value = float(value)
        # for key in params_d:
        #     value_d = params_d[key]
        #     print("@value,type",type(value_d))
        #     # print("key:value",key,value_d)
        #     if (len(value_d)):
        #         print("@value len:",len(value_d))
        #         if (key == "unit"):
        #             unit = value_d
        #         elif (key == "value"):
        #             value = float(value_d)
        #         elif (key == "examtype"):
        #             examtype = value_d
        # 方案2:
        # 如果传入的query参数为空("")(一般是apifox中自动添加的无值参数),或者不传入该参数,那么默认为days
        # 换句话说,如果有query参数被传入,且传入的关键query参数是非空值,那么才将默认值覆盖掉
        # 准备第二套值(不直接影响前面的默认值组)
        unit_tmp = params_d.get("unit")
        value_tmp = params_d.get("value")
        examtype_tmp = params_d.get("examtype")
        if (unit_tmp):
            unit = unit_tmp
        if (value_tmp):
            value = float(value_tmp)
        if (examtype_tmp):
            examtype = examtype_tmp
        # unit = params_d.get("unit", "days")
        # value = params_d.get("value", 8)

        print("@params:", unit, value, examtype)

        # 只需要使用字典打包以下关键字参数
        d = {unit: value}
        delta = timedelta(**d)
        study_ob = QuerysetDispatcher.get_queryset_study(examtype=examtype)

        # delta = timedelta({unit: value})

        # 您不需要如下的负责判断
        # if (unit == 'days'):
        #     delta = timedelta(days=value)
        # elif (unit == 'hours'):
        #     delta = timedelta(hours=value)
        # else:
        #     print("unit的取值是hours或者days!")
        # 注意这里我们通过user来过滤
        queryset = study_ob.filter(user=pk)
        queryset = queryset.filter(last_see_datetime__gte=timezone.now() - delta)

        return Res(NeepStudyModelSerializer(instance=queryset, many=True).data)

    def progress(self, req, pk, examtype):
        progress = 0
        # if (examtype == "neep"):
        querysetDispatcher = QuerysetDispatcher()
        study_ob = querysetDispatcher.get_queryset_study(examtype=examtype)
        progress = study_ob.filter(user=pk).count()

        # & neep_study_ob.filter(examtype=neep)
        return Res({"user": pk, "examtype": examtype, "progress": progress})

    def rank(self, req, pk):
        signin_pk: int = self.queryset.get(pk=pk).signin
        rank = self.queryset.filter(signin__gt=signin_pk).count() + 1
        users_sum = self.queryset.count()
        data = {"rank": rank, "percentage": rank / users_sum, "singin": signin_pk}
        return Res(data)

    def signin(self, req, pk):
        """ 签到天数加一"""
        print("@pk=", pk)
        # 同故通过post动作提交请求信息(包含在请求头中)
        print(f"req.data={req}")

        print(f"req.data={req.data}")
        # rest_framework.mixins.UpdateModelMixin def update(self,
        #            request: {data},
        #            *args: Any,
        #            **kwargs: Any) -> Response
        ##我们调用DRF的UpdateModelMixin提供的更新方法update
        # self.update(req, pk)
        # 但是此处只需要自增signin即可
        """分部操作(get&save)的两种方式"""
        # user = uob.get(pk=pk)
        # # user.signin += 1
        # # 使用F()提高并发安全性和执行效率
        # user.signin = F('signin') + 1
        # user.save()
        # # 使用了F()表达式,我们必须重新拆执行查询,否则会报错(对象发生了变化)
        # # An F() object represents the value of a model field,
        # # transformed value of a model field, or annotated column.
        # # It makes it possible to refer to model field values and perform database operations
        # # using them without actually having to pull them out of the database into Python memory.
        # user = uob.get(pk=pk)
        """方式2:对queryset:F()&update()"""
        user = uob.filter(pk=pk)  # 这里的user是一个QuerySet
        user.update(signin=F('signin') + 1)
        user = uob.get(pk=pk)

        # F() 除了用于上述对单个实例的操作外，F() 还可以与 update() 一起用于对象实例的 QuerySets。
        # 这就把我们上面使用的两个查询——get() 和 save() 减少到只有一个：
        # reporter = Reporters.objects.filter(name='Tintin')
        # reporter.update(stories_filed=F('stories_filed') + 1)

        ser = UserModelSerializer(instance=user)
        # return Res({"msg": f"{ser.data}"})
        return Res(ser.data)

    def review_list(self, req, pk, examtype="neep"):
        """ 获取复习列表(全局) """
        study_ob = QuerysetDispatcher.get_queryset_study(examtype=examtype)
        queryset = study_ob.filter(familiarity__lte=4)  # 只查询不熟的
        queryset = queryset.filter(user=pk)
        if (len(queryset)):
            ser = NeepStudyModelSerializer(instance=queryset, many=True)
            return Response(ser.data)
        return Response("empty...")

    @deprecated
    def review(self, req, pk):
        examtype = "neep"
        if (examtype == "neep"):
            queryset = neep_study_ob.filter(familiarity_lte=4) & neep_study_ob.filter(user=pk)
            ser = NeepStudyModelSerializer(instance=queryset, many=True)
            return Response(ser.data)
        return Response("empty...")

    #     pass

    # action装饰可以提供基于CRUD的extra actions(DRF的界面中也会体现出
    # 登录本身不太容易通过restful 描述
    #    @action(methods=["get"],detail=False,url_path="user/login")
    # @action(methods=["post"],detail=True)
    # def sign_in(self,req,pk):
    #     print("@pk=",pk)
    #     # 同故通过post动作提交请求信息(包含在请求头中)
    #     print(f"req.data={req}")
    #
    #     print(f"req.data={req.data}")

    # self.save(req,pk)

    @action(methods=["get", "post"], detail=False)
    # http://127.0.0.1:8000/user/user_ModelViewSet/login_detail/
    def login(self, req):
        # 查看action
        print(self.action)
        return Response({"msg": "login success!"})

    @action(methods=["get"], detail=True)
    # http://127.0.0.1:8000/user/user_ModelViewSet/2/login_detail/
    def login_detail(self, req, pk):
        return Response({"msg": pk})

    @action(methods=["get"], detail=True, url_path="user_p/login_pd")
    # url_path所指定的url段可以映射到下面的方法
    # http://127.0.0.1:8000/user/user_ModelViewSet/2/user_p/login_pd/
    def login_pathed_detail(self, req, pk):
        return Response({"msg": pk})

    # 用户名作为参数,查找相关用户
    @action(methods=["get"], detail=False)
    def filter_names(self, req):
        """http://127.0.0.1:8000/api/user_ModelViewSet/filter_names/?pattern=create"""
        # queryset=uob.filter(name__contains="cxxu")
        # self.queryset
        if (req.query_params):
            pattern = req.query_params.get("pattern")
            print(f"@pattern={pattern}")
            query = self.get_queryset().filter(name__contains=pattern)
            print(req.query_params)
        else:
            # ser=uob.all()
            query = uob.all()
        ser = UserModelSerializer(instance=query, many=True)
        return Res(ser.data)
        return Response(req.query_params)

    def schedule(self, req, pk=1):
        # self.retrieve(req,pk)
        schedule = get_object_or_404(User, pk=pk).schedule
        # return Response({"msg": "schedault"})
        return Response({"user": pk, "schedule": schedule})


class UserRegisterModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterModelSerializer

    # 可以指定action的url段
    # http://
    # 在序列化器中重写create 方法
    def create(self, request, *args, **kwargs):
        # 首先通过打印判断此类下的drf的create方法会调用序列化器中的create方法还是viewset中的create方法.
        print("@create :: class:", self.__class__.__name__)
        # 对传入的密码进行加密处理:
        # 使用make_password()得到加密后的串这种方式不如自己编写来的可控,尽管它足够安全和方便
        # 着主要体现在盐值的设置上,这个盐值是随机生成的,即使相同的密码加密后的结果是不同的
        # 为了方便验证的进行,我们需要保存盐值,以便进行验证
        # password_hash = make_password(request.data.get("password"))
        md5 = hashlib.md5()
        password_salt = random.randint(1000, 9999)
        print("@salt=", password_salt)
        password_salted_str = str(password_salt) + request.data.get("password", "123")
        print("@password_salted_str=", password_salted_str)
        password_salted_bytes = password_salted_str.encode("utf-8")
        md5.update(password_salted_bytes)
        # 得到字符串形式的加密结果
        password_hash = md5.hexdigest()

        # 查看make_password加密效果(部分结果)
        # print("@create :: passoword_hash:", password_hash[:10])
        # data = request.data
        # print("@request.data:", data, type(data))
        # data["password_hash"] = password_hash
        # print(data)
        # request.data = data
        request.data["password_hash"] = password_hash
        request.data["password_salt"] = password_salt
        # print("@request.data:", request.data, request)
        res = super().create(request)
        # Response(的status是位置参数)
        return Res(res.data, status.HTTP_201_CREATED)
        return Res("test create")
