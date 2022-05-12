from deprecated.classic import deprecated
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user.models import User, WordSearchHistory, WordStar

uob = User.objects


# 外部验证函数(可以用户多个模型共享,但是不多见);定义完成后,需要改通过参数的形式添加到指定的序列化类中字段的构造器(validators=[chekcerxxx]参数)
def name_common_checker(value):
    if "cxxu" not in value.lower():
        raise serializers.ValidationError("the user is created by cxxu")
    return value


"""
什么时候声明的序列化器需要继承序列化器基类Serializer，什么时候继承模型序列化器类ModelSerializer?
1 继承序列化器类serializer
    2 字段声明
    3 验证
    4 添加/保存数据功能
5 继承模型序列化器类ModelSerializer
    字段声明[可选,看需要]
    7 Meta声明
    8 验证
    9 添加/保存数据功能[可选]
看数据是否从mysqI数据库中获取，如果是则使用ModelSerializer，不是则使用Serializer I

"""


# 只用最基本的Serializer类来实现serializer(不使用ModelSerializer中的功能)
# 该序列化器的名称后缀以基本的Serializer结尾
@deprecated
class UserSerializer(serializers.Serializer):
    # 定义元数据类
    class Meta:
        # 指定序列化器是使用的模型类
        model = User
        # 指明使用的字段是给模型的全部字段.
        fields = "__all__"
        #     可以通过数组,指定个别字段
        # fields = ["name", "signin", "signupdate", ]

    #     指定嵌套(关联)深度

    # 基本的校验方式:通过指定字段的参数来传递限制条件
    name = serializers.CharField(max_length=30)
    signin = serializers.IntegerField(max_value=10000, min_value=0, error_messages={
        "min_value": "the sign in days must be:age>=0",
        "max_value": "the Age filed must be:age<=10000 "
    })

    # 序列化器检查数据是否合规
    '''serializer 是直接和数据请求/提交打交道,将数据规范性检查也一并安排在模型的序列化器中是实现'''

    # 针对某些字段实现更加复杂的验证规则
    # 需要以validate_filedName的格式来定义变量名,否则is_validate()无法知道这个检测规则以及该规则适用于哪个字段的检测
    def validate_name(self, value):
        # if "cxxu" not in value.lower():
        #     raise serializers.ValidationError("the user is created by cxxu")
        if value in ["null", "python", "django"]:
            raise serializers.ValidationError(detail="the student name must not be python/django/null",
                                              code="validate_name")
        return value

    # 为序列号器实现update方法,使得序列化器能够帮助我们完成数据更新
    # 在ModelSerializer中,会自动帮我们实现两个方法(create()/update())
    def update(self, instance, validated_data):
        # instance.name = validated_data.get("name", instance.name)
        # instance.signin = validated_data.get("signin", instance.signin)
        # 通过遍历来设置
        for key, value in validated_data.items():
            #     Sets the named attribute on the given object to the specified value.
            # setattr(x, 'y', v) is equivalent to ``x.y = v''
            setattr(instance, key, value)
        instance.save()
        return instance

    # 向数据库添加数据
    def create(self, validated_data):
        """
        方法名固定为create,且参数也是固定名为validate_date
        :param validated_data: 该参数就是验证成功后的结果
        :return: 返回模型对象User实例
        """
        user = uob.create(**validated_data)
        return user


# 单词收藏序列化器
class WordStarModelSerializer(ModelSerializer):
    class Meta:
        model = WordStar
        fields = "__all__"
        # fields = ["id", "spelling", "user_name","user_signin"]
        # fields=["id","user_info","spelling"]
        #在外键引用者中指定关联深度(被反向查询的深度)
        depth = 0
        depth = 1


# 继承于ModelSerializer来编写比较简化的代码
# 该序列化器的名称以ModelSerializer结尾
class UserModelSerializer(serializers.ModelSerializer):
    # 可以编写数据模型之外的子字段在此处:
    # 也可以放置在read_only数组中
    # 注意这里的字段要只读,一般数据库是没有相应字段,在在这里声明,只用于查询数据的时候展示,不写入
    nickname = serializers.CharField(default="testNickname", read_only=True)
    """序列化器嵌套"""
    # 嵌套调用序列化器
    # 对外键模型做反向查询,外键表对象想要知道哪些对象引用了自己
    # 注意名字必须是外键名(更准确的说,是related_name所指定的名字,可以防止名字冲突)
    # (这个名字是定义在外键引用者模型中)(被引用者中不体现)
    # user = UserModelSerializer()
    # 如果反向查询到多个对象,那么需要传入构造参数many=True
    # user_word_star = WordStarModelSerializer(many=True)
    """方式1"""
    # user = UserModelSerializer()
    # user_word_star = WordStarModelSerializer(many=True)
    # 指定depth,应该在外表对应的序列化器中指定depth
    # 当然,一个表(模型)可以对应创建多个序列化器
    """方式2:可以减少json深度"""
    # user_name=serializers.CharField(source="user.name")
    # user_signin=serializers.IntegerField(source="user.signin")
    #
    """使用模型中自定义方法"""


    class Meta:
        # ModelSerialzier内部会使用到Meta内类中的model字段来获取模型进行分析
        model = User
        fields = "__all__"
        # 如果需要包含模型之外的字段,在上方单独定义字段
        # fields = ["uid", "name", "signin", "nickname","user_word_star" ]  # "nickname"
        # 注意,属性方法被fields="__all__"囊括,您需要显式的将字段卸载fields
        # 幸运的是,我们通常也是通过逐个指定白名单来提供给客户端
        # http://127.0.0.1:8000/user/user_info/ (注意DRF的分页功能,数据较少,请在page1检查)
        # fields = ["uid", "name", "signin", "nickname","alias" ]  # "nickname"

        read_only_fields = ["sex", "birthday"]  # 因为是只读,所以旨在序列化(将数据库读出的数据对象转换为指定格式(json...)
        extra_kwargs = {
            "signin": {
                "min_value": 0,
                "max_value": 100000,
                "error_messages": {
                    "min_value": "sign should meet :sign>=0",
                    "max_value": "sign should meet :sign<100000"
                }
            }
        }
        # depth = 1

    """update & create
        def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        # 遍历实例字段
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)
                
        instance.save()
        
        """
    # 在ModelSerializer中,会自动帮我们实现两个方法(create()/update())
    # 但是如果需求比较复杂,就需要重写对应的方法(override)
    # 譬如说,我们要加密用户上传上来的密码,然后在入库
    # 重写也一般是基于被继承的函数添加一些东系(譬如数据加密,然后在调用父类的被重载函数)
    # def create(self, validated_data):
    #     pass


class WSHModelSerializer(ModelSerializer):
    # user_search
    class Meta:
        model = WordSearchHistory
        # fields = ["user"]
        fields = "__all__"
